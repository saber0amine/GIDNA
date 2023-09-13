from django import forms
from realisation.models import Realisation
from lists.models import Projet
from lists.models import Emplacement
from objectif.models import Objectif
from planification.models import Planification
from django.contrib.auth.models import User


class RealisationForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(RealisationForm, self).__init__(*args, **kwargs)
        self.fields['projet'].queryset = Projet.objects.filter(user=user)
        self.fields['emplacement'].queryset = Emplacement.objects.filter(user=user)
        self.fields['obj'].queryset = Objectif.objects.filter(user=user)
        self.fields['tache'].queryset = Planification.objects.filter(user=user)
        self.fields['hrs_est'].queryset = Planification.objects.filter(user=user)

    class Meta:
        model = Realisation
        fields = ['projet' , 'emplacement' , 'obj' , 'tache' , 'livrable' , 'hrs_est' , 'hr_attr']
        widgets = {
            'projet': forms.Select(attrs={'class': 'selected-project-real', 'placeholder': 'Choose your project'}),
            'emplacement': forms.Select(attrs={'class': 'selected-Nature-real', 'placeholder': 'Choose your nature'}),
            'obj': forms.Select(attrs={'class': 'selected-Objectif-real', 'placeholder': 'Choose your objectif'}),
            'tache': forms.Select(attrs={'class': 'selected-task-real', 'placeholder': 'Describe the task'}),  # Changed the name to 'selected-task'
            'livrable': forms.FileInput(attrs={'class': 'selected-livrable-real','accept': 'image/*,application/pdf'}),
            'hrs_est': forms.Select(attrs={'class': 'selected-hrs-est-real', 'placeholder': 'Estimated hours'}),  # Changed the name to 'selected-hrs-est'
            'hr_attr': forms.NumberInput(attrs={'class': 'selected-hr-attr-real','placeholder': 'Attributed hours'}),
        }

 