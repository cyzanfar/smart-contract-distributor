from django.db import models
from django import forms 

# Create your models here.
class Question(models.Model): 
	question_text= models.CharField(max_length=200)
	pub_dat = models.DateTimeField('date published')


class Choice(models.Model): 
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)


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