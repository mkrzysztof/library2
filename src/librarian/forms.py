from django import forms

class IdReaderForm(forms.Form):
    id = forms.UUIDField(label='id czytelnika')
