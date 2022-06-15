from django import forms


class EventoForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre del Evento')
    due_date = forms.DateField(label='Fecha de Evento', widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
    )