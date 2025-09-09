from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_models import Base
import os

# Use environment variable for database URL (for production)
# Falls back to local development URL
db_url = os.getenv("DATABASE_URL", "postgresql://postgres:12345678@localhost:5432/telusko")

# Add connection pooling and error handling
engine = create_engine(
    db_url,
    pool_pre_ping=True,  # Verify connections before use
    pool_recycle=300,    # Recycle connections every 5 minutes
    echo=False           # Set to True for debugging
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        # Create tables if they don't exist
        Base.metadata.create_all(bind=engine)
        yield db
    finally:
        db.close()