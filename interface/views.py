import json
from django.shortcuts import render
import os
from data.bsd import videos_data 


def youtube_home(request):
    videos = videos_data.get('videos', [])
    return render(request, 'index.html', {'videos': videos})
