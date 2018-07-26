from echo.serializers import EchoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EchoView(APIView):
    def get(self, request, format=None):
        serializer = EchoSerializer(data={'number': request.GET['number']})
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = EchoSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
