from django import forms

class IdReaderForm(forms.Form):
    id = forms.IntegerField(label='id czytelnika')

class IdBookForm(forms.Form):
    id = forms.IntegerField(label='id książki')
