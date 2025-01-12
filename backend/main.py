"""
Main application entry point for a FastAPI web server.

This script initializes the FastAPI application, configures middleware, logging, and
routes. It also includes optional instrumentation for Prometheus metrics.

Modules Used:
- `loggers`: Provides logging functionality, including a chat logger instance.
- `middlewares`: Contains middleware definitions and configuration helpers.
- `routes`: Defines the API routes for the application.

Attributes:
- `app` (FastAPI): The main FastAPI application instance.
- `logger`: Logger instance created using `get_chat_logger()`.

Optional Components:
- Prometheus metrics instrumentation (commented out by default) can be enabled
  to monitor and expose application metrics via Prometheus.

Usage:
- Run this script to start the FastAPI application.
- Add or modify middleware, routes, or additional configurations as required.

Example:
Run the application using a suitable ASGI server (such as `uvicorn`):
    uvicorn main:app --host 0.0.0.0 --port 8000
"""

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