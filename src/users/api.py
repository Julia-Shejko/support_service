from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet
from shared.serializers import ResponseMultiSerializer, ResponseSerializer
from users.serializers import UserLightSerializer, UserRegistrationSerializer, UserSerializer, UserUpdateSerializer

User = get_user_model()


class UserAPISet(ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        context: dict = {"request": self.request}

        serializer = UserRegistrationSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        queryset = User.objects.all()

        serializer = UserLightSerializer(queryset, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})

        return JsonResponse(response.data)

    def retrieve(self, request, id_: int):
        instance = User.objects.get(id=id_)

        serializer = UserSerializer(instance)
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def update(self, request, id_: int):
        instance = User.objects.get(id=id_)
        context: dict = {"request": self.request}

        serializer = UserUpdateSerializer(instance, data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data, status=status.HTTP_201_CREATED)


user_create = UserAPISet.as_view({"post": "create"})
users_list = UserAPISet.as_view({"get": "list"})
user_retrieve = UserAPISet.as_view({"get": "retrieve"})
user_update = UserAPISet.as_view({"put": "update"})
