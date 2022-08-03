from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
import re

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def cook_helper(request):
    dish = {}
    text = request.path
    recipe = re.search('(\w+)', text).group(1)
    servings = int(request.GET.get('servings', 1))
    for ingridient, number in DATA[recipe].items():
        dish[ingridient] = number * servings
    context = {'recipe': dish}
    return render(request, 'calculator/index.html', context)
