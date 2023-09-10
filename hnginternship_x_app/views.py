from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
#from django.http import 

from rest_framework.views import APIView
from rest_framework.response import Response

import json
from datetime import datetime, timezone

# Create your views here.
class Index(APIView):
    
    def get(self, request):
        slack_name = request.query_params['slack_name']
        track = request.query_params['track']
        
        today = datetime.today().weekday()
        utc_time = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        day_of_the_week = {
            0:"Monday",
            1:"Tuesday",
            2:"Wednesday",
            3:"Thursday",
            4:"Friday",
            5:"Saturday",
            6:"Sunday",
            }
        context = {
            "slack_name": slack_name,
            "current_day": day_of_the_week[today],
            "utc_time": f"{utc_time}",
            "track": track,
            "github_file_url": "https://github.com/PrinceSamuelAdeyemo/hnginternship_x/blob/main/hnginternship_x_app/views.py",
            "github_repo_url": "https://github.com/PrinceSamuelAdeyemo/hnginternship_x",
            "status_code": HttpResponse.status_code,
        }
        
        return HttpResponse(json.dumps(context, indent=2), content_type="application/json")