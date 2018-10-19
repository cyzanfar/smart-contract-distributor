from django import forms
from .models import Token, Holder

class TokenForm(forms.ModelForm):
    class Meta:
        model = Token
        fields = ['company_name', 'token_name', 'token_supply', 'address']
    # company_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'style': 'border-color: blue;',
    #             'placeholder': 'ICO company name'
    #         }
    #     )
    # )
    # token_name = forms.CharField()
    # token_supply = forms.IntegerField()
    # address = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'style': 'border-color: blue;',
    #             'placeholder': 'ETH Address'
    #         }
    #     )
    # )

class HolderForm(forms.ModelForm):
    class Meta:
        model = Holder
        fields = ['percent_stake']

HolderFormSet = forms.inlineformset_factory(Token, Holder, form=HolderForm, extra=3)
