from django.db import models

class Token(models.Model):
    company_name=models.CharField(max_length=150)
    name=models.CharField(max_length=150)
    supply=models.BigIntegerField()
    address=models.CharField(max_length=150)

class Holder(models.Model):
    token=models.ForeignKey(Token,related_name='holders',on_delete=models.CASCADE)
    percent_stake=models.DecimalField(max_digits=3,decimal_places=2)
    wallet_address=models.CharField(max_length=150)
    user_type=models.CharField(max_length=150)
