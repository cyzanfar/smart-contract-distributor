from django import forms
from .models import Token, Holder

class TokenForm(forms.ModelForm):
    class Meta:
        model = Token
        fields = ['company_name', 'token_name', 'token_supply', 'address']

class HolderForm(forms.ModelForm):
    class Meta:
        model = Holder
        fields = ['percent_stake']

HolderFormSet = forms.inlineformset_factory(Token, Holder, form=HolderForm, extra=1)
