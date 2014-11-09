from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from estimote.models import Datapoint
from estimote.serializers import DatapointSerializer

# Create your views here.
class JSONResponse(HttpResponse):
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, kwargs)

@csrf_exempt
def datapoint_list(request):
	if request.method == "GET":
		datapoints = Datapoint.objects.all()
		serializer = DatapointSerializer(datapoints, many = True)
		return JSONResponse(serializer.data)	
	elif request.method == "POST":
		data = JSONParser().parse(request)
        serializer = DatapointSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
