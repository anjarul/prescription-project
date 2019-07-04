from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import PrescriptionAddForm
from .models import Prescription


# @login_required
def add_prescription(request, user=None):

    if request.method == 'POST':
        form = PrescriptionAddForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = PrescriptionAddForm()

    template = 'prescription/add_prescription.html'
    context = {'form': form}

    return render(request, template, context)
