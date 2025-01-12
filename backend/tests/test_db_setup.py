import unittest
from sqlalchemy import inspect, create_engine
from sqlalchemy.orm import sessionmaker
from backend.models.models import Base


class TestDatabaseSetup(unittest.TestCase):
    """
    Unit tests for database setup and configuration.
    """

    def setUp(self):
        """
        Set up an in-memory SQLite database before each test.
        """
        # Use an in-memory database to avoid interacting with the actual database file.
        self.test_engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
        self.TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.test_engine)

        # Create the tables in the in-memory database for testing.
        Base.metadata.create_all(bind=self.test_engine)

    def tearDown(self):
        """
        Drop all tables and dispose of the engine after each test.
        """
        Base.metadata.drop_all(bind=self.test_engine)
        self.test_engine.dispose()

    def test_engine_creation(self):
        """
        Test if the engine is created successfully and connected to the database.
        """
        with self.test_engine.connect() as connection:
            self.assertIsNotNone(connection)
            self.assertTrue(connection.closed == False)

    def test_sessionlocal_factory(self):
        """
        Test if the SessionLocal factory produces valid sessions.
        """
        session = self.TestSessionLocal()
        self.assertIsNotNone(session)

        # Test if the session can be used to insert and retrieve data (example with no actual data here)
        session.close()

    def test_table_creation(self):
        """
        Verify that all tables defined in Base are created in the database.
        """
        inspector = inspect(self.test_engine)  # Use SQLAlchemy's inspector to check database schema
        tables = inspector.get_table_names()
        self.assertGreater(len(tables), 0, "No tables were created in the database.")

    # Additional tests can be written for specific models or data insertion logic
    # if needed.


if __name__ == "__main__":
    unittest.main()