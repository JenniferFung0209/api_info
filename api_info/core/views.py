from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class InfoView(APIView):
    @swagger_auto_schema(
        operation_description="Proporciona información general sobre la API.",
        responses={200: openapi.Response('Información general operativa')}
    )
    def get(self, request):
        """
        Devuelve información general sobre el estado y propósito de la API.
        """
        return Response({'información': 'API con información general operativa'}, status=status.HTTP_200_OK)
