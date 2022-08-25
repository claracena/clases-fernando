'''
Pete, the baker

Pete likes to bake some cakes. He has some recipes and ingredients.
Unfortunately he is not good in maths. Can you help him to find out, how many
cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available
ingredients (also an object) and returns the maximum number of cakes Pete can
bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb
of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not
present in the objects, can be considered as 0.

Examples:

# must return 2
cakes(
    {flour: 500, sugar: 200, eggs: 1},
    {flour: 1200, sugar: 1200, eggs: 5, milk: 200}
)
# must return 0
cakes(
    {apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100},
    {sugar: 500, flour: 2000, milk: 2000}
)
'''




















# My answer
def cakes_1(recipe, available):
    response = 0

    for ingredient in recipe:
        qty = 0
        if ingredient not in available:
            return 0
        else:
            if recipe[ingredient] > available[ingredient]:
                return 0
            else:
                qty = available[ingredient] // recipe[ingredient]
                if response > 0:
                    if qty > 0 and qty < response:
                        response = qty
                else:
                    response = qty
        
    return response

# Some answers submitted as example
def cakes_2(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)

def cakes_3(recipe, available):
    try:
        return min([available[a]/recipe[a] for a in recipe])
    except:
        return 0

def cakes_4(recipe, available):
    ''' Take each ingredient from the recipe, see if it is in the available ones
        and calculate how many full cakes you can make with it.
        If an ingredient is missing, we can't bake a cake. Otherwise we have to
        find the lowest possible amount of cakes.'''
    return min([available[i]//recipe[i] if i in available else 0 for i in recipe])

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
# recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
# available = {"sugar": 500, "flour": 2000, "milk": 2000}

# print(cakes_1(recipe, available))
# print(cakes_2(recipe, available))
# print(cakes_3(recipe, available))
# print(cakes_4(recipe, available))
