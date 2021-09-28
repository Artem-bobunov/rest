from django.forms import ModelForm
from rest_framework import serializers
from django_rest.models import meterReadings

#ModelForm
class restSerializer(ModelForm):
    class Meta:
        model = meterReadings
        fields = "__all__"
