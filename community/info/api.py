from django import views


from rest_framework import viewsets
from .models import Person
from . import serializers
class Personviewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class=serializers.PersonSerializer
    # permission_classes=((IsSuperUserOrReadOnly,))


