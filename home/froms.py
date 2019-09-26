from django import forms
from home import models
from parent.models import Parent 
from driver.auto_complete import RelatedFieldWidgetCanAdd

class StudentForm(forms.ModelForm):

    class Meta:
        model = models.Students
        fields = ('__all__')
        widgets = {
            'parent':
            RelatedFieldWidgetCanAdd(
                related_model=Parent,
                url="/auto-complete/parent/"
            )
        }
