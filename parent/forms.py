from django import forms
from parent import models


class ParentForm(forms.ModelForm):

    class Meta:
        model = models.Parent
        fields = ('__all__')
