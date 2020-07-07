# my-fastapi

Python `fastapi` framework example starter.

# Setup

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
  pip freeze > requirements.txt
  pip install -r requirements.txt
  ```

1. To run the code in file `main.py`, and start uvicorn with:
   ```
   uvicorn main:app --reload
   ```

# Essentials

- [ ] one unit test
- [ ] one end point
- [ ] code coverage - `https://codecov.io/`
- [ ] flake
- [ ] github action
- [ ] build a docker image
- [ ] sonarcube
