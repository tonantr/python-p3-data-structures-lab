spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [key['name'] for key in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [foods for foods in spicy_foods if foods['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    [
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}') for food in spicy_foods
    ]

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # return [food for food in spicy_foods if food['cuisine'] == cuisine]
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    [
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}') for food in spicy_foods if food['heat_level'] > 5
    ]

def get_average_heat_level(spicy_foods):
    size = len(spicy_foods)
    total = 0
    average_heat_level = 0
    for food in spicy_foods:
        total = total + food['heat_level']
        average_heat_level = int(total / size)
    return average_heat_level
    
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods



