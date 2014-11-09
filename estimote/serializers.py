from django.forms import widgets
from rest_framework import serializers
from estimote.models import Datapoint

class DatapointSerializer(serializers.ModelSerializer):
	class Meta:
		model = Datapoint
		fields = ('id','date','distance','minor')