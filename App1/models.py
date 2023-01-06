from django.db import models


class courseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) <5 :
            errors['name'] = "course name should be more than 5 characters"
        if len(postData['desc']) < 15:
            errors['desc'] = "course description should be more than 15 characters"
        return errors

class course(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    objects=courseManager()

def show_course():
    return course.objects.all()

def add_course(request):
    return course.objects.create(name=request.POST['name'],description=request.POST['desc'])

def destroy_course(request,course_id):
    return course.objects.get(id=course_id)
    
def delete_course(request,course_id):
   ncourse=course.objects.get(id=course_id)
   return ncourse.delete()