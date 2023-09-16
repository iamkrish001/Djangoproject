from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def write(req):
    return render(req, "lorem.html")   #used  render function to display the html template lorem.html

def list_all_students(req):
    from .models import Student
    from django.shortcuts import redirect
    if req.method == 'POST':
        name = req.POST['name']
        email = req.POST['email']
        roll_no = req.POST['roll_no']
        bio = req.POST['bio']
        obj = Student()
        obj.name = name
        obj.email = email
        obj.roll_no = roll_no
        obj.bio = bio
        obj.save()
        return redirect('/')
    else:
        students = Student.objects.all()
        context = {
        "no_students"  : students  }
        return render(req, "index.html ", context  )
