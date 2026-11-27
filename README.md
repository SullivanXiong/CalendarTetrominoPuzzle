# CalenderTetrominoPuzzle

A solver for my calender Tetromino puzzle

# Setup

add this to your environment activate script to enable automatic module discovery

linux/unix/macOS
export PYTHONPATH="$VIRTUAL_ENV/calender_solver:$PYTHONPATH"

Windows Powershell
$env:PYTHONPATH = "$env:VIRTUAL_ENV\calender_solver;" + $env:PYTHONPATH

CMD
set PYTHONPATH=%VIRTUAL_ENV%\calender_solver;%PYTHONPATH%

# Run the tests

From the repository root, after `uv sync --frozen`:

```sh
PYTHONPATH=. .venv/bin/python -m unittest discover -s calendar_solver/test -t .
```
