from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from driver import models
from driver import forms
from django.db.models import ProtectedError
from django.views import View

def delete(request, model, pk):
    model_table = getattr(models, model)
    obj = model_table.objects.get(id=pk)
    try:
        obj.delete()
        return HttpResponse(obj)
    except ProtectedError:
        return HttpResponse(model, status=409)


class EditTaxi(View):

    def get_object(self, pk):
        try:
            return models.Taxi.objects.get(id=pk)
        except:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        form = forms.TaxiForm(instance=obj)
        return render(request, 'taxi/edit.html', {'form': form})

    def post(self, request, pk):
        obj = self.get_object(pk)
        form = forms.TaxiForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('taxi')
        return render(request, 'taxi/edit.html', {'form': form})


class EditDriver(View):

    def get_object(self, pk):
        try:
            return models.Driver.objects.get(id=pk)
        except:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        form = forms.DriverForm(instance=obj)
        return render(request, 'driver/edit.html', {'form': form})

    def post(self, request, pk):
        obj = self.get_object(pk)
        form = forms.DriverForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('driver')
        return render(request, 'driver/edit.html', {'form': form})
