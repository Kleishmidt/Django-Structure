from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.contact.serializers import ConsultationSerializer
from core import settings


# Generic Email Sending View
class EmailSendView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = None
    email_subject = 'Contact Form Submission'

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email_content = self.get_email_content(serializer.validated_data)
            if not self.send_email(email_content):
                return Response({'error': 'Failed to send email'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response({'message': f'Email message were sent successfully'},
                            status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_email(self, email_content):
        try:
            send_mail(self.email_subject, email_content, settings.EMAIL_HOST_USER, [settings.EMAIL_RECEIVER])
            return True
        except Exception as e:
            return e

    def get_email_content(self, validated_data):
        pass


class ConsultationEmailSendView(EmailSendView):
    serializer_class = ConsultationSerializer

    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request):
        return super().post(request)

    def get_email_content(self, validated_data):
        return f'First Name: {validated_data.get("first_name")}\nLast Name: {validated_data.get("last_name")}\n' \
               f'Phone: {validated_data.get("phone")}\nEmail: {validated_data.get("email")}\n' \
               f'Instagram: {validated_data.get("instagram")}\nContact choice: {validated_data.get("contact_choice")}'
