
from rest_framework.viewsets import ModelViewSet
from ..models import TaxBracket
from .serializers import TaxBracketSerializer


class TaxBracketViewSet(ModelViewSet):
    """A View set for  TaxBracket"""

    serializer_class = TaxBracketSerializer
    queryset = TaxBracket.objects.all()
