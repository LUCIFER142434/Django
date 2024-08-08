from django.shortcuts import render

def hello_world(element):
    return render (element,'hello.html')


