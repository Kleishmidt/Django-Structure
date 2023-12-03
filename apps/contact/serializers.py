from rest_framework import serializers


class ConsultationSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=40)
    last_name = serializers.CharField(max_length=40)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=15, required=False)
    message = serializers.CharField(max_length=500, required=False)
