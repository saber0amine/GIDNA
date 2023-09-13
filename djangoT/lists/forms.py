from django import forms
from .models import Projet
from .models import Nature
from .models import Emplacement


class ProjetForm(forms.ModelForm):
    
    class Meta:
        model =Projet
        fields = ['projet']

class NatureForm(forms.ModelForm):
    
    class Meta:
        model =Nature
        fields = ['nature']
        
class EmplacementForm(forms.ModelForm):
    
    class Meta:
        model =Emplacement
        fields = ['emplacement']

class UpdateProjetForm(forms.ModelForm):

    class Meta:

        model = Projet
        fields = ['projet']
        
class UpdateNatureForm(forms.ModelForm):
    
    class Meta:
        model =Nature
        fields = ['nature']

class UpdateEmplacementForm(forms.ModelForm):
    
    class Meta:
        model = Emplacement
        fields = ['emplacement']
