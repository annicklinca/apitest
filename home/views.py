from pyexpat.errors import messages
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from django.http import HttpResponse, JsonResponse
import requests
from .serializers import *
import hashlib
import random
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
# Create your views here.

@csrf_exempt
def  welcome(request):
    

    if request.method == "POST":
        message = NewsLetter(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            phone = request.POST.get('phone'),
        )
        message.save()
        name = message.email
        messages.success(request, f"Thank you for subsribing to ournews Letter")
        return redirect('home')
    else:
        return render(request, 'index.html', context)



# contact us

@csrf_exempt
def addproduct(request):
   
    if request.method == 'GET':
        reg = Product.objects.all()
        serializer = ProductSerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request) #request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successful'}, status=201)
        return JsonResponse(serializer.errors, status=400)  



  
