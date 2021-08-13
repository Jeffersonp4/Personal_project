from django.forms import ModelForm, PasswordInput

from class_date.models import conexs_pool


class connex_Form(ModelForm):
    class Meta:
        model = conexs_pool
        fields = '__all__'
        widgets = {

            'password': PasswordInput(attrs={'type': 'password'})
        }