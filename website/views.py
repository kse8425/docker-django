from django.shortcuts import render, redirect
import random

# Create your views here.
from website.models import Person


def index(request):
    members = Person.objects.all().order_by('-id')
    return render(request, 'website/index.html', {'members': members})


def person(request):
    members = ['조남제', '송성한', '성주은', '김성은', '김주영', '이나훈', '최예원']
    likse = ['사과', '딸기', '바나나', '키위', '수박', '복숭아', '파인애플']
    input_data = {
        'name': random.choice(members),
        'like': random.choice(likse),
    }
    Person.objects.create(**input_data)
    return redirect('website:index')
