from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django_tables2 import RequestConfig
from driver import tables
from driver import forms
from driver import filters
from driver import models
from django.contrib import messages


class TaxiView(View):

    def get(self, request):
        return self.add(request) if 'add' in request.GET \
            else self.display(request)

    def add(self, request):
        form = forms.TaxiForm()
        return render(request, 'taxi/add.html', {'form': form})

    def display(self, request):
        taxi_filter = filters.TaxiFilter(request.GET)
        taxis = models.Taxi.objects.all().order_by('-id')
        taxi_table = tables.TaxiTable(taxis)
        RequestConfig(request, paginate={'per_page': 50}).configure(
            taxi_table)
        context = {'table': taxi_table, 'filter': taxi_filter}
        return render(request, 'taxi/display.html', context)

    def post(self, request):
        form = forms.TaxiForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'taxi' + form.data['name'] + 'Added')
            return redirect('taxi')
        return render(request, 'taxi/add.html', {'form': form})


class DriverView(View):

    def get(self, request):
        return self.add(request) if 'add' in request.GET \
            else self.display(request)

    def add(self, request):
        form = forms.DriverForm()
        return render(request, 'driver/add.html', {'form': form})

    def display(self, request):
        driver_filter = filters.DriverFilter(request.GET)
        drivers = models.Driver.objects.all().order_by('-id')
        driver_table = tables.DriverTable(drivers)
        RequestConfig(request, paginate={'per_page': 50}).configure(
            driver_table)
        context = {'table': driver_table, 'filter': driver_filter}
        return render(request, 'driver/display.html', context)

    def post(self, request):
        form = forms.DriverForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Driver' + form.data['name'] + 'Added')
            return redirect('driver')
        return render(request, 'driver/add.html', {'form': form})