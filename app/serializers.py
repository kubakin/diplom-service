from rest_framework import serializers
from .models import History, Visitor, TestData
class HistoryListSerializer(serializers.ModelSerializer):
    # user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model= History
        fields='__all__'
class HistoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=History
        fields = '__all__'
class HistoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=History
        fields = '__all__'
class VisitorSerializer(serializers.Serializer):
    #  user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model= Visitor
        fields='__all__'
class TestDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestData
        fields='__all__'