def cakes(recipe, available):
    return min([available[x]//recipe[x] if x in available else 0 for x in recipe])