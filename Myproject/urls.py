
from django.contrib import admin
from django.urls import path
from app.views import write  # importing write function from app.views
from app.views import list_all_students 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('write/', write),
    path("", list_all_students)
]
