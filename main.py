import sys
import groceryasst

plan = groceryasst.top_level.weeklyPlan()

# plan.mealList()


response = groceryasst.api_man.findMealWeb("breakfast")


print(response.text)
