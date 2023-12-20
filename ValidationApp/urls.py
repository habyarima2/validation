# ValidationApp/urls.py
from django.urls import path
from .views import add_participant, add_vehicle, register_vehicle, success_page

urlpatterns = [
    path('', add_participant, name='add_participant'),
    path('add_vehicle/', add_vehicle, name='add_vehicle'),
    
    path('success_page_vehicle/<int:participant_id>/', success_page, name='success_page_vehicle'),
    path('success_page/', success_page, name='success_page_vehicle'),
    
    
]
