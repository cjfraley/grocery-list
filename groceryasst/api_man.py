import yaml
import random
import pkg_resources
import requests

actual_random = random.SystemRandom()

try:
    with open("conf/plan.yaml", "r") as stream:
        try:
            plan=yaml.load(stream)
        except yaml.YAMLError as exc:
            print("A problem was found in your plan config file")
            raise(exc)
except:
    print("No plan file found. Going with defaults.")
    # with open("conf/default_plan.yaml", "r") as stream:
    stream=pkg_resources.resource_stream("groceryasst", "default_conf/plan.yaml")
    try:
        plan=yaml.load(stream)
    except yaml.YAMLError as exc:
        print("A problem was found in your plan config file")
        raise(exc)
def refresh_cache():
    stream=pkg_resources.resource_stream("groceryasst", "default_conf/basic_meals.yaml")
    try:
        meal_lib=yaml.load(stream)
        # if type(custom_meals)=="dict":
    except yaml.YAMLError as exc:
        print("A problem was found in the basic meals file")
        raise(exc)
    with open("meal_lib/cache.yaml", "r") as stream:
        try:
            cache_meals=yaml.load(stream)
            if type(cache_meals)=="dict":
                meal_lib={**meal_lib, **custom_meals}
        except yaml.YAMLError as exc:
            print("A problem was found in your meal cache file")
            raise(exc)
    with open("meal_lib/custom.yaml", "r") as stream:
        try:
            custom_meals=yaml.load(stream)
            if type(custom_meals)=="dict":
                meal_lib={**meal_lib, **custom_meals}
        except yaml.YAMLError as exc:
            print("A problem was found in custom meals file")
            raise(exc)
    return meal_lib

def findMeal(type_of_meal, meal_plan):
    meal_lib=refresh_cache()
    yaml.dump(meal_lib)
    doesnt_fit=True
    while doesnt_fit:
        list_of_meals=list(meal_lib.keys())
        meal_name=actual_random.choice(list_of_meals)
        meal_from_lib=meal_lib[meal_name]
        if meal_from_lib["type"]==type_of_meal:
            print("Found matching meal: "+meal_name)
            return meal_name
        else:
            continue
    # mealName=random
    # mealName=meal_lib.keys[randint(len(meal_lib.keys()))]
    # return "gruel"

def findMealWeb(type_of_meal):
    payload={}
    if type_of_meal in ["dessert","breakfast"]:
        payload["type"]=type_of_meal
    if "dislikes" in plan.keys():
        payload["excludeIngredients"]=plan["dislikes"]
    if "diet" in plan.keys():
        payload["diet"]=plan["diet"]
    return search(payload)

def search(payload):
    # Have to figure out using these types
    # The type of the recipes. One of the following: main course, side dish, dessert, appetizer, salad, bread, breakfast, soup, beverage, sauce, or drink.
    response = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/searchComplex",
        params=payload,
        headers={
            "X-RapidAPI-Key": "K4PobKJKIOmshR7r7VuGzz8cleYtp10dlJojsnOSGbIyPY0rWe"
        }
    )
    return response
