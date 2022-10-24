from importlib.resources import path
from django.urls import include, path
from . import views


# one urlpattern per line
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.saas_app4, name='saas_app4'),
    path('create-project/', views.createProject, name='create-project'),
    path('update-project/<str:pk>/', views.updateProject, name="update-project"),
    # path('saas_app4', views.saas_app4, name='saas_app4'),
    path('single_saas_app/<str:pk>/', views.single_saas_app, name='single_saas_app'),
    path('delete-object/<str:pk>)/', views.deleteProject, name='delete-object'),
    path('admin-approval/', views.admin_approval, name='admin-approval'),
    path('reforms/', views.reforms, name='reforms'),
    path('reform_form/', views.create_reform, name='reform_form'),
]

# '' : empty string and /
# views.index : index function in views.py
# name='index' : name of the route