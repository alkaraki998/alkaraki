from django.contrib import admin
from django.urls import path, include
from my_app import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('my_app.urls')),
    url(r'add_todo/', views.add_todo),
    path('delete_todo/<int:todo_id>/', views.delete_todo)

]
