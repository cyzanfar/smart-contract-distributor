from django.db import models
from django import forms

class Token(models.Model):
    company_name = models.CharField(max_length=150)
    token_name = models.CharField(max_length=150)
    token_supply = models.BigIntegerField()
    address = models.TextField()
    #name
    #value
    #initial token holders
    #address of the ethereum smart contract that holds the token

class Holder(models.Model):
	token = models.ForeignKey(Token, on_delete=models.CASCADE)
	percent_stake = models.DecimalField(max_digits=3, decimal_places=2)
	#vested = models.BooLeanField()
