from django.urls import include,path
from .views import index
urlpatterns=[
    path('',index.as_view(),name='index')
]