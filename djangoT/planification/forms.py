from .models import Planification 
from lists.models import Projet 
from lists.models import Nature 
from django import forms
from objectif.models import Objectif
# class DateInput(forms.DateTimeInput):
#      input_type = 'date'

class PlanificationForm(forms.ModelForm):
    obj = forms.ModelChoiceField(queryset=Objectif.objects.all(), to_field_name='id', widget=forms.Select(attrs={'class': 'selected-Nature'}))
    def __init__(self, user, *args, **kwargs):
        super(PlanificationForm, self).__init__(*args, **kwargs)
        # Filter the 'projet' and 'nature' choices based on the logged-in user
        self.fields['projet'].queryset = Projet.objects.filter(user=user)
        self.fields['nature'].queryset = Nature.objects.filter(user=user)
        self.fields['obj'].queryset = Objectif.objects.filter(user=user)

    class Meta:
        model = Planification
        fields = ['projet' , 'nature','tache', 'hrs_est' ,'livrable' , 'obj' ]

        widgets = {
            'projet': forms.Select(attrs={'class': 'selected-project-plan', 'placeholder': 'Choose your project'}),
            'nature': forms.Select(attrs={'class': 'selected-Nature-plan', 'placeholder': 'Choose your nature'}),
            'tache': forms.Textarea(attrs={'class': 'selected-tache-plan','placeholder': 'Describe the task'}),
            'livrable': forms.TextInput(attrs={'class': 'selected-livrable-plan','placeholder': 'Enter the deliverable'}),
            'hrs_est': forms.NumberInput(attrs={'class': 'selected-hour-plan','placeholder': 'Estimated hours'}),
        }
        
        
class UpdateTacheForm(forms.ModelForm):
        
    class Meta:
        model = Planification
        fields = ['projet' , 'nature','tache', 'hrs_est' ,'livrable' , 'obj' ]
    

    