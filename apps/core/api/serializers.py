from rest_framework import serializers

from ..models import TaxBracket


class TaxBracketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxBracket
        fields = "__all__"
