################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# ===== CLASS FOR MAGICAL OVEN =====
class MagicalOven:
  
  RECIPES = {
    ("water", "air"): {"freeze": "snow"},
    ("lead", "mercury"): {"boil": "gold"},
    ("cheese", "dough", "tomato"): {"boil": "pizza"}
  }
  
  def __init__(self):
    # Initialize an empty list of ingredients
    self.ingredients = []
      
  def add(self, item):
    # Append the ingredient to the list
    self.ingredients.append(item)
      
  def freeze(self):
    self.ingredients = self._combine_ingredients("freeze")

  def boil(self):
    self.ingredients = self._combine_ingredients("boil")

  def wait(self):
    # Modify ingredients based on waiting rules
    self.ingredients = self._combine_ingredients("wait")
    
  def get_output(self):
    return self.ingredients[0] if len(self.ingredients) == 1 else self.ingredients

  def _combine_ingredients(self, method):
    rules = [
      (["water", "flour"], "boil", "dough"),
      (["lead", "mercury"], "boil", "gold"),
      (["water", "air"], "freeze", "snow"),
      (["cheese", "dough", "tomato"], "boil", "pizza"),
    ]
    
    for rule in rules:
      if set(self.ingredients) == set(rule[0]) and method == rule[1]:
        return [rule[2]]
    
    return self.ingredients
            
# This function should return an oven instance!
def make_oven():
  return MagicalOven()

def alchemy_combine(oven, ingredients, temperature):
  
  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()

  return oven.get_output()