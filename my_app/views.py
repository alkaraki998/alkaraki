from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from requests.compat import quote_plus  # ADDS + IN THE URL WHEN THEY USE SAPCE
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from my_app.models import Todo


# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    stuff_for_frontend = {"todo_items": todo_items}
    return render(request, 'my_app/index.html', stuff_for_frontend)


@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    Todo.objects.create(text=content, added_date=current_date)
    return HttpResponseRedirect("/")


@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
