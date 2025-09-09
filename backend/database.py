from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_models import Base
import os

# Use environment variable for database URL (for production)
# Falls back to local development URL
db_url = os.getenv("DATABASE_URL", "postgresql://postgres:12345678@localhost:5432/telusko")
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        # Create tables if they don't exist
        Base.metadata.create_all(bind=engine)
        yield db
    finally:
        db.close()