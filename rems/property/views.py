from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Property, Tenant
from .forms import PropertyForm, TenantAssignmentForm

@login_required
def property_list(request):
    p = Property.objects.all()
    context = {
        "properties": p
    }
    return render(request, 'property_list.html',context)


@login_required
def property_retrieve(request, pk):
    p = Property.objects.get(id=pk)
    u = p.units.all()
    context = {
        "property": p,
        "units": u
    }
    return render(request, 'property_detail.html', context)


@login_required
def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    form = PropertyForm()
    context = {
        'form': form
    }
    return render(request, 'property_create.html', context)


def assign_tenant_to_unit(request):
    if request.method == 'POST':
        form = TenantAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success/')  # Redirect to a success page or another URL
    else:
        form = TenantAssignmentForm()

    return render(request, 'tenant_assignment.html', {'form': form})


def success_page_view(request):
    return render(request, 'tenant_assigned_success.html')

