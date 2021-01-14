## Document
[https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)

## Commands
Serve: `$ uvcorn main:app --reload`

## Dependencies
1. `pyjwt` - For JWT encode/decode. Link [https://github.com/jpadilla/pyjwt](https://github.com/jpadilla/pyjwt).
1. `passlib` - For Bcrypt encode. Link [https://pypi.org/project/passlib/](https://pypi.org/project/passlib/).
1. `aiofiles` - For serving static files. Link [https://pypi.org/project/aiofiles/](https://pypi.org/project/aiofiles/).
1. `pytest` - For testing. [https://docs.pytest.org/en/stable/](https://docs.pytest.org/en/stable/).

## Static Files
Link: [http://localhost:8000/static/files/test.txt](http://localhost:8000/static/files/test.txt)

## Deployment
Using `gunicorn` for serving in production. \
Command `$ gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app` (include pid file, etc.). \
Read more on [https://www.uvicorn.org/deployment/](https://www.uvicorn.org/deployment/).