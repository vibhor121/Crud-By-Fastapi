#!/usr/bin/env python3
"""
Script to create database tables using SQLAlchemy Base.metadata.create_all()
"""
from database_models import Base
from database import engine

def create_all_tables():
    """Create all tables defined in database_models using Base.metadata.create_all()"""
    print("🚀 Creating database tables using Base.metadata.create_all()...")
    print(f"Database URL: postgresql://postgres:12345678@localhost:5432/telusko")
    print("-" * 60)
    
    try:
        # This is the line you wanted to see!
        Base.metadata.create_all(bind=engine)
        print("✅ All tables created successfully!")
        
        # Show what tables were created
        print("\n📋 Tables created:")
        for table_name in Base.metadata.tables.keys():
            print(f"  - {table_name}")
            
        print("\n🎉 Database setup complete!")
        print("\nYou can now view the tables in pgAdmin:")
        print("1. Open pgAdmin 4")
        print("2. Navigate to: telusko → Schemas → public → Tables")
        print("3. You should see the 'products' table")
        
    except Exception as e:
        print(f"❌ Error creating tables: {e}")

if __name__ == "__main__":
    create_all_tables()

