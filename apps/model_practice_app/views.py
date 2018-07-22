from django.shortcuts import render

# Create your views here.
#  import our db
from .models import *

def index(request):
    context = {"authors": Author.objects.all()}
    return render(request, "model_practice_app/index.html", context)