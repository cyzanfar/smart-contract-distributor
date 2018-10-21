from rest_framework import serializers
from django.contrib.auth.models import User
from contract.models import Token, Holder

class HolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holder
        fields = ('id', 'percent_stake', 'user_type')

class TokenSerializer(serializers.ModelSerializer):
    holders = HolderSerializer(many=True)

    class Meta:
        model = Token
        fields = (
            'id', 'company_name', 'name',
            'supply', 'address', 'holders'
        )

    def create(self, validated_data):
        import pdb; pdb.set_trace()
        holders_data = validated_data.pop('holders')
        token = Token.objects.create(**validated_data)
        for holder_data in holders_data:
            Holder.objects.create(token=token, **holder_data)
        return token

class UserSerializer(serializers.ModelSerializer):
    tokens = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Token.objects.all()
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'tokens')
