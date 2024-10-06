import { reactive } from "vue";

export const state = reactive({
    meals: [],

    defaultFoodTypes: [
        { label: "Cereais", code: "CEREAIS" },
        { label: "Verduras", code: "VERDURAS" },
        { label: "Frutas", code: "FRUTAS" },
        { label: "Gorduras e óleos", code: "GORDURAS_OLEOS" },
        { label: "Pescados", code: "PESCADOS" },
        { label: "Carnes", code: "CARNES" },
        { label: "Leites", code: "LEITES" },
        { label: "Bebidas", code: "BEBIDAS" },
        { label: "Ovos", code: "OVOS" },
        { label: "Açucarados", code: "ACUCARADOS" },
        { label: "Miscelaneas", code: "MISCELANEAS" },
        { label: "Industrializados", code: "INDUSTRIALIZADOS" },
        { label: "Preparados", code: "PREPARADOS" },
        { label: "Leguminosas", code: "LEGUMINOSAS" },
        { label: "Nozes", code: "NOZES" },
    ],

    defaultMeals: [
        {
            title: "Café da manhã",
            typesSelected: ["CEREAIS", "FRUTAS", "LEITES", "OVOS", "NOZES"],
            target: {
                servings: 5,
                calories: 700,
                proteins: 15,
                lipids: 14,
                carbohydrates: 75,
                fibers: 8,
            },
        },
        {
            title: "Almoço",
            typesSelected: [
                "Verduras",
                "Gorduras e óleos",
                "Pescados",
                "Carnes",
                "Ovos",
                "Bebidas",
                "Preparados",
                "Leguminosas",
            ],
            target: {
                servings: 8,
                calories: 1000,
                proteins: 24,
                lipids: 22,
                carbohydrates: 90,
                fibers: 10,
            },
        },
        {
            title: "Janta",
            typesSelected: [
                "Pescados",
                "Frutas",
                "Verduras",
                "Industrializados",
                "Preparados",
                "Miscelâneas",
            ],
            target: {
                servings: 4,
                calories: 300,
                proteins: 25,
                lipids: 20,
                carbohydrates: 100,
                fibers: 7,
            },
        },
    ],
});
