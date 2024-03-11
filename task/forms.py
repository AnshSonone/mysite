from django.forms import ModelForm
from .models import *

class Videoform(ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'