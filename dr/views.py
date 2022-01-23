from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def download(res):
    if res.method == "POST":
        print(res.POST)
    return render(res, 'otp.html', {})
