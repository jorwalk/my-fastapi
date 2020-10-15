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

## Essentials

- [x] one unit test
- [x] one end point
- [x]
- [x] code coverage - `https://codecov.io/`
- [x] flake
- [x] github action
- [x] build a docker image

1. An example workflow that uses GitHub Actions to deploy to Cloud Run.
   - https://github.com/GoogleCloudPlatform/github-actions/blob/master/example-workflows/cloud-run/README.md

## Helpful Links

- [How to set up GitHub workflows and create GitHub Actions using Docker](https://itnext.io/how-to-set-up-github-workflows-and-create-github-actions-using-docker-3a5ba7ec0988)

- [FastAPI — authentication revisited: Enabling API key authentication](https://medium.com/data-rebels/fastapi-authentication-revisited-enabling-api-key-authentication-122dc5975680)
