from django.db import models

class Token(models.Model):
    company_name = models.CharField(max_length=150)
    token_name = models.CharField(max_length=150)
    token_supply = models.BigIntegerField()
    address = models.CharField(max_length=150)

class Holder(models.Model):
	token = models.ForeignKey(Token, on_delete=models.CASCADE)
	percent_stake = models.DecimalField(max_digits=3, decimal_places=2)
