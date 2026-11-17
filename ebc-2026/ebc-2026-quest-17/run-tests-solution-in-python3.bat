:: TODO: Symbolic link to shared helpers (if needed) in Microsoft Windows
:: md /c mklink /D .\solution-in-python3\helpers ..\..\shared\shared_python3\helpers

::rm .\solution-in-python3\helpers\*_helper.py
::rmdir .\solution-in-python3\helpers
xcopy /s /i /Y ..\..\shared\shared_python3\helpers .\solution-in-python3\helpers 

python3 -m pytest -v