from rest_framework import serializers
from django.contrib.auth.models import User
from contract.models import Token, Holder

class TokenSerializer(serializers.ModelSerializer):    
    holders = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Holder.objects.all()
    )

    class Meta:
        model = Token
        fields = (
            'id', 'company_name', 'token_name',
            'token_supply', 'address', 'holders'
        )


class HolderSerializer(serializers.ModelSerializer):
    token = serializers.CharField(source='token.pk')

    class Meta:
        model = Token
        fields = ('id', 'user_type', 'token', 'percent_stake')

class UserSerializer(serializers.ModelSerializer):
    tokens = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Token.objects.all()
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'tokens')
