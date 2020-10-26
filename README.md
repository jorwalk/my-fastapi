# My FastAPI python library starter

Python `fastapi` framework example starter.

## Action Workflow Status

- ![Python application](https://github.com/jorwalk/my-fastapi/workflows/Python%20application/badge.svg?branch=master)
- [![codecov](https://codecov.io/gh/jorwalk/my-fastapi/branch/master/graph/badge.svg)](https://codecov.io/gh/jorwalk/my-fastapi)

# Setup

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
pip install package && pip freeze > requirements.txt
git push --set-upstream origin develop
```

1. To run the code in file `main.py`, and start uvicorn with:

   ```
   uvicorn main:app --reload
   ```

1. To run the code coverage
   ```
   coverage run
   ```
