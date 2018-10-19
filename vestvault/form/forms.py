from django import forms

class TokenForm(forms.Form):
    company_name = forms.CharField(max_length=150)
    token_name = forms.CharField(max_length=150)
    token_supply = forms.BigIntegerField()
    address = forms.TextField()

class HolderForm(forms.Form):
	percent_stake = forms.DecimalField(max_digits=3, decimal_places=2)


    # def clean(self):
    #     cleaned_data = super(ContactForm, self).clean()
    #     name = cleaned_data.get('name')
    #     email = cleaned_data.get('email')
    #     message = cleaned_data.get('message')
    #     if not name and not email and not message:
    #         raise forms.ValidationError('You have to write something!')
