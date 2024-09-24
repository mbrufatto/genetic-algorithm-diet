from app import db

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    moisture_percent = db.Column(db.Float, nullable=False, default=0)
    energy_kcal = db.Column(db.Float, nullable=False, default=0)
    energy_kl = db.Column(db.Float, nullable=False, default=0)
    protein_g = db.Column(db.Float, nullable=False, default=0)
    lipids_g = db.Column(db.Float, nullable=False, default=0)
    cholesterol_mg = db.Column(db.Float, nullable=False, default=0)
    carbohydrate_g = db.Column(db.Float, nullable=False, default=0)
    dietary_fiber_g = db.Column(db.Float, nullable=False, default=0)
    ash_g = db.Column(db.Float, nullable=False, default=0)
    calcium_mg = db.Column(db.Float, nullable=False, default=0)
    magnesium_mg = db.Column(db.Float, nullable=False, default=0)
    manganese_mg = db.Column(db.Float, nullable=False, default=0)
    phosphorus_mg = db.Column(db.Float, nullable=False, default=0)
    iron_mg = db.Column(db.Float, nullable=False, default=0)
    sodium_mg = db.Column(db.Float, nullable=False, default=0)
    potassium_mg = db.Column(db.Float, nullable=False, default=0)
    copper_mg = db.Column(db.Float, nullable=False, default=0)
    zinc_mg = db.Column(db.Float, nullable=False, default=0)
    retinol_mcg = db.Column(db.Integer, nullable=False, default=0)
    re_mcg = db.Column(db.Float, nullable=False, default=0)
    rae_mcg = db.Column(db.Float, nullable=False, default=0)
    thiamine_mg = db.Column(db.Float, nullable=False, default=0)
    riboflavin_mg = db.Column(db.Float, nullable=False, default=0)
    pyridoxine_mg = db.Column(db.Float, nullable=False, default=0)
    niacin_mg = db.Column(db.Float, nullable=False, default=0)
    vitamin_c_mg = db.Column(db.Float, nullable=False, default=0)
    category = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'moisture_percent': self.moisture_percent,
            'energy_kcal': self.energy_kcal,
            'energy_kl': self.energy_kl,
            'protein_g': self.protein_g,
            'lipids_g': self.lipids_g,
            'cholesterol_mg': self.cholesterol_mg,
            'carbohydrate_g': self.carbohydrate_g,
            'dietary_fiber_g': self.dietary_fiber_g,
            'ash_g': self.ash_g,
            'calcium_mg': self.calcium_mg,
            'magnesium_mg': self.magnesium_mg,
            'manganese_mg': self.manganese_mg,
            'phosphorus_mg': self.phosphorus_mg,
            'iron_mg': self.iron_mg,
            'sodium_mg': self.sodium_mg,
            'potassium_mg': self.potassium_mg,
            'copper_mg': self.copper_mg,
            'zinc_mg': self.zinc_mg,
            'retinol_mcg': self.retinol_mcg,
            're_mcg': self.re_mcg,
            'rae_mcg': self.rae_mcg,
            'thiamine_mg': self.thiamine_mg,
            'riboflavin_mg': self.riboflavin_mg,
            'pyridoxine_mg': self.pyridoxine_mg,
            'niacin_mg': self.niacin_mg,
            'vitamin_c_mg': self.vitamin_c_mg,
            'category': self.category
        }