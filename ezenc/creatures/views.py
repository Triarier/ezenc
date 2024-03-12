from django.shortcuts import render

from creatures.models import Creature
import sys
import plotly.express as px
import pandas as pd


def index(request):
    print(f"Current directory: {sys.path}")
    creature_list = Creature.objects.all()
    for creature in creature_list:
        df = pd.DataFrame(
            dict(
                r=[
                    creature.strength,
                    creature.dexterity,
                    creature.constitution,
                    creature.intelligence,
                    creature.wisdom,
                    creature.charisma,
                ],
                theta=[
                    "Strength",
                    "Dexterity",
                    "Constitution",
                    "Intelligence",
                    "Wisdom",
                    "Charisma",
                ],
            )
        )
        fig = px.line_polar(df, r="r", theta="theta", line_close=True)
        fig.update_layout(polar_radialaxis_showticklabels=False)
        creature.radar = fig.to_html(
            full_html=False, default_height=300, default_width=300
        )
    context = {
        "creature_list": creature_list,
    }
    return render(request, "creatures/index.html", context)
