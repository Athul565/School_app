from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from parent import models
from parent import forms
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


class EditParent(View):

    def get_object(self, pk):
        try:
            return models.Parent.objects.get(id=pk)
        except:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        form = forms.ParentForm(instance=obj)
        return render(request, 'parent/edit.html', {'form': form})

    def post(self, request, pk):
        obj = self.get_object(pk)
        form = forms.ParentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('parent')
        return render(request, 'parent/edit.html', {'form': form})
