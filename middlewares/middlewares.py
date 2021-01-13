from fastapi import FastAPI, Request


def init_middlewares(app: FastAPI):

    @app.middleware("http")
    async def auth_middleware(request: Request, call_next):
        response = await call_next(request)
        print("auth_middleware hitted!")
        return response
