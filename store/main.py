from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from store.core.config import settings
from store.core.exceptions import CreateException, NotFoundException
from store.routers import api_router


class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            **kwargs,
            version="0.0.1",
            title=settings.PROJECT_NAME,
            root_path=settings.ROOT_PATH
        )


app = App()
app.include_router(api_router)

@app.exception_handler(NotFoundException)
async def not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=404,
        content={"detail": exc.message},
    )

# @app.exception_handler(CreateException)
# async def create_exception_handler(request: Request, exc: CreateException):
#     return JSONResponse(
#         status_code=500,
#         content={"detail": exc.message},
#     )

# @app.exception_handler(BaseException)
# async def base_exception_handler(request: Request, exc: BaseException):
#     return JSONResponse(
#         status_code=500,
#         content={"detail": exc.message},
#     )