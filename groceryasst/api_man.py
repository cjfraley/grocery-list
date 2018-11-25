import yaml
import random
import pkg_resources

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

def findMeal(meal, meal_plan):
    meal_lib=refresh_cache()
    yaml.dump(meal_lib)
    doesnt_fit=True
    while doesnt_fit:
        list_of_meals=list(meal_lib.keys())
        meal_name=random.choice(list_of_meals)
        meal_from_lib=meal_lib[meal_name]
        if meal_from_lib["type"]==meal:
            print("Found matching meal: "+meal_name)
            return meal_from_lib
        else:
            continue
    # mealName=random
    # mealName=meal_lib.keys[randint(len(meal_lib.keys()))]
    # return "gruel"
