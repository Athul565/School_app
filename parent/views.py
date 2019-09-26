from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django_tables2 import RequestConfig
from parent import tables
from parent import forms
from parent import filters
from parent import models
from django.contrib import messages

# Create your views here.

class ParentView(View):

    def get(self, request):
        return self.add(request) if 'add' in request.GET \
            else self.display(request)

    def add(self, request):
        form = forms.ParentForm()
        return render(request, 'parent/add.html', {'form': form})

    def display(self, request):
        parent_filter = filters.ParentFilter(request.GET)
        parents = models.Parent.objects.all().order_by('-id')
        parent_table = tables.ParentTable(parents)
        RequestConfig(request, paginate={'per_page': 50}).configure(
            parent_table)
        context = {'table': parent_table, 'filter': parent_filter}
        return render(request, 'parent/display.html', context)

    def post(self, request):
        form = forms.ParentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Parent' + form.data['name'] + 'Added')
            return redirect('parent')
        return render(request, 'parent/add.html', {'form': form})
