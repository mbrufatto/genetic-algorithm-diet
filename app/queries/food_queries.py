from sqlalchemy.orm import Session
from sqlalchemy import func
from ..models.food import Food


def get_all_food(db: Session):
    return db.query(Food).all()


def get_food_by_category_list(db: Session, categories=None):
    if categories:
        categories_lower = [category.lower() for category in categories]
        foods = db.query(Food).filter(func.lower(Food.category).in_(categories_lower)).all()
        return foods
    else:
        return get_all_food(db)


def get_foods_by_category(db: Session, category=str):
    return db.query(Food).filter(Food.category == category)
