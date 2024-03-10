from django.shortcuts import render

from creatures.models import Creature
import sys


def index(request):
    print(f"Current directory: {sys.path}")
    creature_list = Creature.objects.all()
    context = {
        "creature_list": creature_list,
    }
    return render(request, "creatures/index.html", context)
