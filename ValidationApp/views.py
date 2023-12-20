# ValidationApp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ParticipantForm, VehicleForm
from .models import Participant, Vehicles
from django.forms import formset_factory


def add_participant(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save()
            return redirect('success_page_vehicle', participant_id=participant.id)
    else:
        # Modify the form instantiation to include placeholder text
        form = ParticipantForm(initial={
            
        })

    return render(request, 'add_participant.html', {'form': form})

def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save()
            return redirect('success_page', vehicle_id=vehicle.id)
    else:
        
        form = VehicleForm(initial={
            
        })

    return render(request, 'add_vehicle.html', {'form': form})

def register_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save()
            participant = vehicle.participant  # Assuming there's a ForeignKey in Vehicles model to Participant
            return redirect('success_page', vehicle_id=vehicle.id)
    else:
        # Modify the form instantiation to include placeholder text
        form = VehicleForm(initial={
            
        })

    return render(request, 'register_vehicle.html', {'form': form})

def success_page(request, participant_id=None, vehicle_id=None):
    context = {}
    
    if participant_id:
        participant = get_object_or_404(Participant, id=participant_id)
        context['participant'] = participant

    if vehicle_id:
        vehicle = get_object_or_404(Vehicles, id=vehicle_id)
        context['vehicle'] = vehicle

    return render(request, 'success_page.html', context)



