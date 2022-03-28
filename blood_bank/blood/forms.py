from django import forms
from .models import Donor, Branch


class DonorCreationForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-filed'
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    gender = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    mobile = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Donor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')
