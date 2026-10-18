import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def word_in_grid_east_with_wrap(word, grid, r, c):
    matches = set()
    ri = r
    ci = c
    cols = len(grid[0])
    for wc in word:
        cell = grid[ri][ci]
        if wc != cell:            
            return None
        matches.add((ri, ci))
        ci = (ci + 1) % cols        
    return matches


def word_in_grid_west_with_wrap(word, grid, r, c):
    matches = set()
    ri = r
    ci = c
    cols = len(grid[0])
    for wc in word:
        cell = grid[ri][ci]
        if wc != cell:            
            return None
        matches.add((ri, ci))
        ci = (ci - 1) % cols        
    return matches


def word_in_grid_south_without_wrap(word, grid, r, c):
    matches = set()
    ri = r
    ci = c
    rows = len(grid)
    
    for i, wc in enumerate(word):
        cell = grid[ri][ci]
        logger.debug(f"word={word} r={r} c={c} cell={cell}")
        if wc != cell:            
            return None
        matches.add((ri, ci))

        if i == len(word) -1:
            break

        ri += 1
        if ri >= rows:
            return None        
    return matches


def word_in_grid_north_without_wrap(word, grid, r, c):
    matches = set()
    ri = r
    ci = c
    
    for i, wc in enumerate(word):
        cell = grid[ri][ci]
        if wc != cell:            
            return None
        matches.add((ri, ci))

        if i == len(word) -1:
            break

        ri -= 1
        if ri < 0:
            return None        
    return matches


def solve(filename):
    import file_helper
    import grid_helper

    sections = file_helper.get_text_sections(filename)

    word_section = sections[0][6:]
    words = word_section.split(',')
    logger.debug(f"words={words}")

    grid, rows, cols = grid_helper.to_grid(sections[1])

    logger.debug(f"grid={grid} rows={rows} cols={cols}")

    matches = set()
    for r in range(rows):
        for c in range(cols):
            cell = grid[r][c]
            #logger.debug(f"cell={cell} at r={r} c={c}")

            # for each words check whether matches from current cell 
            for w in words:
                word_matches = word_in_grid_east_with_wrap(w, grid, r, c)
                if word_matches:
                    logger.debug(f"Matched east w={w} word_matches={word_matches}")
                    matches = matches.union(word_matches)

                word_matches = word_in_grid_west_with_wrap(w, grid, r, c)
                if word_matches:
                    logger.debug(f"Matched west w={w} word_matches={word_matches}")
                    matches = matches.union(word_matches)

                word_matches = word_in_grid_south_without_wrap(w, grid, r, c)
                if word_matches:
                    logger.debug(f"Matched south w={w} word_matches={word_matches}")
                    matches = matches.union(word_matches)

                word_matches = word_in_grid_north_without_wrap(w, grid, r, c)
                if word_matches:
                    logger.debug(f"Matched north w={w} word_matches={word_matches}")
                    matches = matches.union(word_matches)


    ans = 0
    for _ in matches:
        ans += 1
    return ans