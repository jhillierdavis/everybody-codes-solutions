def count_flips(s):
    """
    Count the number of flips required to group identical letters together in a string.
    Returns a tuple of (flip_count, letters_reversed, transformed_string).
    """
    chars = list(s)

    flip_count = 0
    letters_reversed = 0

    i = 0
    while i < len(chars):
        letter = chars[i]

        # Current contiguous block
        left_end = i
        while left_end + 1 < len(chars) and chars[left_end + 1] == letter:
            left_end += 1

        while True:
            # Find rightmost block of the same letter
            r = len(chars) - 1
            while r > left_end and chars[r] != letter:
                r -= 1

            if r <= left_end:
                break

            # Extend to the left to find start of that rightmost block
            right_start = r
            while right_start - 1 > left_end and chars[right_start - 1] == letter:
                right_start -= 1

            # Reverse the intervening region including the right block
            start = left_end + 1
            end = r

            chars[start:end + 1] = reversed(chars[start:end + 1])

            flip_count += 1
            letters_reversed += end - start + 1

            # Recompute contiguous block after flip
            while left_end + 1 < len(chars) and chars[left_end + 1] == letter:
                left_end += 1

        i = left_end + 1

    return flip_count, letters_reversed, ''.join(chars)