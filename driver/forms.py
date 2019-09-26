from django import forms
from driver import models
from driver.auto_complete import RelatedFieldWidgetCanAdd


class TaxiForm(forms.ModelForm):
    class Meta:
        model = models.Taxi
        fields = ('__all__')


class DriverForm(forms.ModelForm):

    class Meta:
        model = models.Driver
        fields = ('__all__')
        widgets = {
            'taxi':
            RelatedFieldWidgetCanAdd(
                related_model=models.Taxi,
                url="/auto-complete/taxi/"
            )
        }
