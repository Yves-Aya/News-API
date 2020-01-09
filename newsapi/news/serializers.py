from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from news.models import Article


class ArticleSerializer(serializers.ModelSerializer):
     time_since_publication =serializers.SerializerMethodField() 
     author = serializers.StringRelatedField()

     class Meta:
          model = Article
          fields = "__all__"
     
     def get_time_since_publication(self,object):
         publication_date = object.publication_date
         now = datetime.now()
         time_delta = timesince(publication_date,now)
         return time_delta

     def validate(self, data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and description must be different")
        return data

     def validate_title(self,value):
        if len(value)<6:
            raise serializers.ValidationError("len of title cannot be less than 60 chars long")
        return value 