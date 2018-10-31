import csv
import yaml

def __init__(self):
    try:
        with open("conf/plan.yaml", "r") as stream:
            try:
                plan=yaml.load(stream)
            except yaml.YAMLError as exc:
                print("A problem was found in your plan config file")
                raise(exc)
    except:
        print("No plan file found. Going with defaults.")
        with open("conf/default_plan.yaml", "r") as stream:
            try:
                plan=yaml.load(stream)
            except yaml.YAMLError as exc:
                print("A problem was found in your plan config file")
                raise(exc)
