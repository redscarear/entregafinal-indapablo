from django import forms


class BlogForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre del Posteo')
    due_date = forms.DateField(label='Fecha del Post', widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
    )