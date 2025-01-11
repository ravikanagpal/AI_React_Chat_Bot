from fastapi import FastAPI

from loggers import get_chat_logger
from middlewares import add_middleware
from routes import router

logger = get_chat_logger()

app = FastAPI()
add_middleware(app)

app.include_router(router)

# Add Prometheus metrics instrumentation
# from prometheus_fastapi_instrumentator import Instrumentator
# @app.on_event("startup")
# async def startup():
#     Instrumentator().instrument(app).expose(app)