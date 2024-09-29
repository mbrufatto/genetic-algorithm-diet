import { reactive } from 'vue';

export const state = reactive({
    meals:  [],

    defaultFoodTypes: [
        "Cereais",
        "Verduras",
        "Frutas",
        "Gorduras_Oleos",
        "Pescados",
        "Carnes",
        "Leites",
        "Bebidas",
        "Ovos",
        "Açucarados",
        "Miscelâneas",
        "Industrializados",
        "Preparados",
        "Leguminosas",
        "Nozes"
    ],

    defaultMeals: [
        {
            title: 'Café da manhã',
            typesSelected: ['Cereais','Frutas', 'Leites', 'Ovos','Nozes'],
            target: {
                servings: 5,
                calories: 700,
                proteins: 15,
                lipids: 14,
                carbohydrates: 75,
                fibers: 8,
            }

        },
        {
            title: 'Almoço',
            typesSelected: ['Verduras','Gorduras e óleos',
                'Pescados','Carnes','Ovos','Bebidas','Preparados','Leguminosas'],
            target: {
                servings: 8,
                calories: 1000,
                proteins: 24,
                lipids: 22,
                carbohydrates: 90,
                fibers: 10,
            }
        },
        {
            title: 'Janta',
            typesSelected: ['Pescados','Frutas','Verduras','Industrializados','Preparados','Miscelâneas'],
            target: {
                servings: 4,
                calories: 300,
                proteins: 25,
                lipids: 20,
                carbohydrates: 100,
                fibers: 7,
            }
        },
    ]

})
