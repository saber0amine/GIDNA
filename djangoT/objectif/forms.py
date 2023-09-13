from django import forms
from .models import Objectif, Projet, Nature

class DateInput(forms.DateTimeInput):
    input_type = 'date'

class ObjectifForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(ObjectifForm, self).__init__(*args, **kwargs)
        # Filter the 'projet' and 'nature' choices based on the logged-in user
        self.fields['projet'].queryset = Projet.objects.filter(user=user)
        self.fields['nature'].queryset = Nature.objects.filter(user=user)

    class Meta:
        model = Objectif
        fields = ['projet', 'nature', 'obj', 'date_objectif']
        widgets = {
            'projet': forms.Select(attrs={'class': 'selected-project', 'placeholder': 'choose your project'}),
            'nature': forms.Select(attrs={'class': 'selected-Nature', 'placeholder': 'choose your nature'}),
            'obj': forms.Textarea(attrs={'class': 'selected-objectif', 'placeholder': 'write your objectif'}),
            'date_objectif': DateInput(),
        }

class UpdateObjectifForm(forms.ModelForm):
    class Meta:
        model = Objectif
        fields = ['projet', 'nature', 'obj', 'date_objectif']
