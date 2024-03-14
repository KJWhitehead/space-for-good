from django.shortcuts import render
from .models import Our_Mission

def our_mission_sfg(request):
    """
    Renders the Mission Statement page
    """
    our_mission = Our_Mission.objects.all().order_by('title').first()

    return render(
        request,
        "our_mission/our_mission.html",
        {"our_mission": our_mission},
    )

# Create your views here.
