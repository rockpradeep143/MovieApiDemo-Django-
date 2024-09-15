from rest_framework import serializers
from .models import Moviesdata
class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = Moviesdata
        fields = ['id','name','duration','ratting','image']

