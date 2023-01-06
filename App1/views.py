from django.shortcuts import render,redirect
from. import models
from .models import course
from django.contrib import messages


def index(request):
    context={
        'courses':models.show_course()
    }
    return render(request,'index.html',context)

def addcourse(request):
    if request.method=="POST":
        errors = course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            models.add_course(request)
    return redirect('/')

def destroy(request,course_id):
    context={
        'selected_course':models.destroy_course(request,course_id)
    }
    return render(request,'course.html',context)

def back(request):
    return redirect('/')

def delete(request,course_id):
    if request.method=="POST":
        models.delete_course(request,course_id)
    return redirect('/')
