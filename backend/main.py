from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import Product, ProductCreate
from database_models import ProductDB
from database import get_db

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # React dev server
        "https://your-netlify-app.netlify.app",  # Replace with your Netlify URL
        "https://your-custom-domain.com"  # Replace with your custom domain if you have one
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🚀 This project now uses Model Dumping and Unpacking for cleaner code!

@app.get("/")
def greet():
    return "Hello, World! Cjachupakur"

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        # Test database connection
        db.execute("SELECT 1")
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    try:
        products = db.query(ProductDB).all()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    product = db.query(ProductDB).filter(ProductDB.id == id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/product")
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    # Using model dumping and unpacking - much cleaner! 🚀
    db_product = ProductDB(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.put("/product/{id}")
def update_product(id: int, updated_product: Product, db: Session = Depends(get_db)):
    product = db.query(ProductDB).filter(ProductDB.id == id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Using model dumping and unpacking for updates! 🚀
    # Get the data as dictionary, exclude 'id' since we don't want to update it
    update_data = updated_product.dict(exclude={'id'})
    
    # Update each field using unpacking
    for field, value in update_data.items():
        setattr(product, field, value)
    
    db.commit()
    db.refresh(product)
    return product

@app.delete("/product/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    product = db.query(ProductDB).filter(ProductDB.id == id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}