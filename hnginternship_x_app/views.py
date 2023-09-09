from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

import json
from datetime import datetime

# Create your views here.
class Index(View):
    
    def get(self, request, pk1, pk2):
        slack_name = pk1
        track = pk2
        #return Response("Hello, World");
        context = {
            "slack_name": slack_name,
            "current_day": datetime.date.today,
            "utc_time": datetime.today,
            "track": track,
            #"github_file_url",
            #"github_repo_url",
            #"status_code"
            #"level": level
        }
        
        jsoncontext = json.dumps(context)
        #return HttpResponse(f"{slack_name} and {level}")
        return HttpResponse(jsoncontext)