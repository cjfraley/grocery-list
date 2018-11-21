import csv
import yaml
from . import api_man
import pkg_resources

# from . import default_conf.plan.yaml
# from basic_defs import week
# get day of the week datetime.datetime.today().weekday()


class weeklyPlan(object):
    def __init__(self):
        try:
            with open("conf/plan.yaml", "r") as stream:
                try:
                    self.plan=yaml.load(stream)
                except yaml.YAMLError as exc:
                    print("A problem was found in your plan config file")
                    raise(exc)
        except:
            print("No plan file found. Going with defaults.")
            # with open("conf/default_plan.yaml", "r") as stream:
            stream=pkg_resources.resource_stream("groceryasst", "default_conf/plan.yaml")
            try:
                self.plan=yaml.load(stream)
            except yaml.YAMLError as exc:
                print("A problem was found in your plan config file")
                raise(exc)
    def mealList(self):
        meals_in_day=self.plan["meals_in_day"]
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
            print(day)
            for meal in meals_in_day:
                if day not in self.plan["meals_off"].keys():
                    print("Day "+day+" not listed in meals_off")
                    meal_plan[day][meal]=api_man.findMeal(meal, meal_plan)
                else:
                    if meal not in self.plan["meals_off"][day]:
                        print("Meal "+meal+" of day "+day+" is not listed in meals_off")
                        meal_plan[day][meal]=api_man.findMeal(meal, meal_plan)
        with open("output.yaml", "w") as out:
            yaml.dump(meal_plan, out)
