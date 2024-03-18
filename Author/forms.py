from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields='__all__'
    # name = forms.CharField(label='Name', max_length=100)
    # bdate = forms.DateField(label='bdate')
    # photo = forms.ImageField(label='Photo')


    def clean_author_name(self):
        name = self.cleaned_data['name']
        if Author.objects.filter(name=name).exists():
            raise forms.ValidationError("Aurhor's name already exists")
        if len(name) == 0:
            return name
        else:
            raise forms.ValidationError("Name can't be empty")