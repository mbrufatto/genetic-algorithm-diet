import openpyxl
from app.models.food import Food
from app import db

def safe_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0

def populate_db(drop_database=True):
    if drop_database:
        Food.query.delete()
        db.session.commit()

    if Food.query.first() is None:
        wb = openpyxl.load_workbook('Alimentos.xlsx', data_only=True)
        sheet = wb.active

        for row in sheet.iter_rows(min_row=2, values_only=True):
            name, moisture_percent, energy_kcal, energy_kl, protein_g, lipids_g, cholesterol_mg, carbohydrate_g, dietary_fiber_g, ash_g, calcium_mg, magnesium_mg, manganese_mg, phosphorus_mg, iron_mg, sodium_mg, potassium_mg, copper_mg, zinc_mg, retinol_mcg, re_mcg,  rae_mcg, thiamine_mg, riboflavin_mg, pyridoxine_mg, niacin_mg, vitamin_c_mg, category = row
            food = Food(
                name=name,
                moisture_percent=safe_float(moisture_percent),
                energy_kcal=safe_float(energy_kcal),
                energy_kl=safe_float(energy_kl),
                protein_g=safe_float(protein_g),
                lipids_g=safe_float(lipids_g),
                cholesterol_mg=safe_float(cholesterol_mg),
                carbohydrate_g=safe_float(carbohydrate_g),
                dietary_fiber_g=safe_float(dietary_fiber_g),
                ash_g=safe_float(ash_g),
                calcium_mg=safe_float(calcium_mg),
                magnesium_mg=safe_float(magnesium_mg),
                manganese_mg=safe_float(manganese_mg),
                phosphorus_mg=safe_float(phosphorus_mg),
                iron_mg=safe_float(iron_mg),
                sodium_mg=safe_float(sodium_mg),
                potassium_mg=safe_float(potassium_mg),
                copper_mg=safe_float(copper_mg),
                zinc_mg=safe_float(zinc_mg),
                retinol_mcg=safe_float(retinol_mcg),
                re_mcg=safe_float(re_mcg),
                rae_mcg=safe_float(rae_mcg),
                thiamine_mg=safe_float(thiamine_mg),
                riboflavin_mg=safe_float(riboflavin_mg),
                pyridoxine_mg=safe_float(pyridoxine_mg),
                niacin_mg=safe_float(niacin_mg),
                vitamin_c_mg=safe_float(vitamin_c_mg),
                category=category
            )
            print(f"Food: {name}")
            db.session.add(food)

        db.session.commit()

        print("Banco de dados populado com sucesso")
    else:
        print("Banco de dados já populado")
