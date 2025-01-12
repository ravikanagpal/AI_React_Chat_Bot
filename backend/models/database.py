from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base  # Import the Base class, used for model definitions, from the `models` module

"""
Database configuration module.

This module is responsible for setting up the database connection using SQLAlchemy.
It defines the database URL, initializes the database engine, and configures the session
used to interact with the database. It also ensures that all tables defined in the `models`
module are created in the database if they do not already exist.
"""

# Define the database URL for a SQLite database file named `chat.db`
# The database file will be created in the current working directory.
SQLALCHEMY_DATABASE_URL = "sqlite:///./chat.db"

# Create the SQLAlchemy engine to enable communication with the SQLite database.
# "check_same_thread": False is necessary for SQLite to work with multiple threads.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Configure the SessionLocal class. This class will serve as a factory for new session objects.
# autocommit=False: Ensures that transactions are not automatically committed.
# autoflush=False: Disables automatic flushing of changes to the database before queries.
# bind=engine: Associates this session with the created database engine.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables defined in the `models.py` file (via the `Base` class).
# If the tables already exist in the SQLite database, this operation will be skipped.
Base.metadata.create_all(bind=engine)