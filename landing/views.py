from django.shortcuts import render

def index(r):
    return render(r, 'landing/index.html')

def contact(r):
    return render(r, 'landing/contact.html')