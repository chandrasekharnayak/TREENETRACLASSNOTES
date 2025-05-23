from django.shortcuts import render

# Create your views here.

def user_details(requets):
    return render(requets,'homepage/index.html')
