# My FastAPI python library starter

Python `fastapi` framework example starter.

## Action Workflow Status

- ![Python application](https://github.com/jorwalk/my-fastapi/workflows/Python%20application/badge.svg?branch=master)
- [![codecov](https://codecov.io/gh/jorwalk/my-fastapi/branch/master/graph/badge.svg)](https://codecov.io/gh/jorwalk/my-fastapi)

# Setup

- [x] [Code coverage](https://codecov.io/gh/jorwalk/my-fastapi)
- [ ] create a virtual environment and activate
- [ ] pip install packages
- [ ] pip freeze requirements

  ```shell
  mkdir .my_venv
  python -m venv .my_venv
  source .my_venv/bin/activate
  pip install fastapi[all]
  pip install --upgrade pip
  pip install pytest
  pip install codecov
  pip install coverage
  pip freeze > requirements.txt
  pip install -r requirements.txt
  coverage run -m pytest -s
  coverage html
  ```

1. To run the code in file `main.py`, and start uvicorn with:

   ```
   uvicorn main:app --reload
   ```

1. To run the code coverage
   ```
   coverage run
   ```

# Essentials

- [ ] one unit test
- [ ] one end point
- [ ] code coverage - `https://codecov.io/`
- [ ] flake
- [ ] github action
- [ ] build a docker image
- [ ] sonarcube
