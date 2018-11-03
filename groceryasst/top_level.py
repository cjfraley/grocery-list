import csv
import yaml
from . import api_man
import pkg_resources

# from . import default_conf.plan.yaml
# from basic_defs import week


# def __init__(self):
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

def weeklyPlan():
    print(plan)
    meals_in_day=plan["meals_in_day"]
    grocery_list={}
    meal_plan={
        "mon":{},
        "tues":{},
        "wed":{},
        "thurs":{},
        "fri":{},
        "sat":{},
        "sun":{}
    }
    for day in meal_plan.keys():
        for meal in meals_in_day:
            meal_plan[day][meal]=api_man.findMeal(meal, meal_plan)
    with open("output.yaml", "w") as out:
        yaml.dump(meal_plan, out)
