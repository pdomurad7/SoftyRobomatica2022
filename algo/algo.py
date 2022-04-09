_recipes = {
    'pizza': ['flour', 'tomato', 'cheese', 'salami', 'oil'],
    'spagetti': ['pasta', 'tomato', 'onion', 'salt', 'pork'],
    'tuna salad': ['tuna', 'eggs', 'lettuce', 'salt', 'onion', 'tomato'],
    'french toasts': ['bread', 'milk', 'eggs', 'sugar', 'cheese'],
    'smt': ['pizza']
}

# aval_prod = ['tomato', 'pasta', 'onion', 'salami', 'cheese']
# test_baza = {'Sienkiewicza 5': ['pizza', 'banana', 'wine glass', 'pizza', 'bottle', 'broccoli'],
#              'Krucza 50': ['pizza', 'banana', 'wine glass', 'pizza', 'bottle', 'broccoli']}

def algorithm(database):
    aval_prod = []
    adresses = []
    for key in database:
        aval_prod.extend(database[key])
        adresses.append(key)
    global _recipes
    available_dishes = []
    for k in _recipes:
        if len(_recipes[k]) - len(set(aval_prod) & set(_recipes[k])) <= 2:
            available_dishes.append(k)
    return available_dishes, adresses
# test

