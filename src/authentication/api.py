from django.http import JsonResponse
from rest_framework import status
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from shared.serializers import ResponseSerializer


class _TokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        response = ResponseSerializer({"result": serializer.validated_data})

        return JsonResponse(response.data, status=status.HTTP_200_OK)


class _TokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        response = ResponseSerializer({"result": serializer.validated_data})

        return JsonResponse(response.data, status=status.HTTP_200_OK)
