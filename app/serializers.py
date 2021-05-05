from app.models import Books1
from rest_framework_mongoengine import serializers

class BookSerializer(serializers.DocumentSerializer):
    class Meta:
        model=Books1
    
