from django.urls import path

from .views import add_prescription

app_name = 'prescription'


urlpatterns = [


    path('add-prescription/', add_prescription, name='add-prescription'),

]
