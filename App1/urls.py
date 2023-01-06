from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('add_course',views.addcourse), 
    path('courses/destroy/<int:course_id>',views.destroy),
    path('GoBack',views.back),
    path('course/<int:course_id>/delete',views.delete),
]