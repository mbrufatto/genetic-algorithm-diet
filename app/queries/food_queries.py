from sqlalchemy.orm import Session
from ..models.food import Food

def get_all_food(db: Session):
    return db.query(Food).all()

def get_foods_by_category(db: Session, category=str):
    return db.query(Food).filter(Food.category == category)