from fastapi.middleware.cors import CORSMiddleware


# Function to add middleware to the FastAPI application
def add_middleware(app):
    """
    Adds Cross-Origin Resource Sharing (CORS) middleware to the FastAPI application.

    Parameters:
        app: FastAPI instance to which the middleware is added.

    The middleware allows:
    - All origins to access the application ('allow_origins=["*"]').
    - Credentials (cookies, authorization headers, etc.) to be included in requests ('allow_credentials=True').
    - All HTTP methods (e.g., GET, POST, PUT, DELETE) ('allow_methods=["*"]').
    - All HTTP headers in requests ('allow_headers=["*"]').

    WARNING: Allowing all origins, methods, and headers can be a potential
    security risk for your application. This configuration is typically only
    recommended for development or if you trust all clients accessing your API.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allow all origins to make requests
        allow_credentials=True,  # Enable sending of credentials with requests
        allow_methods=["*"],  # Allow all HTTP methods
        allow_headers=["*"],  # Allow all headers in requests
    )