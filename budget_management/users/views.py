from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from budget_management.users.serializers import UserLoginSerializer, UserSerializer


class SignupView(APIView):
    @swagger_auto_schema(
        operation_summary="유저 회원가입",
        request_body=UserSerializer,
        responses={
            status.HTTP_201_CREATED: UserSerializer,
        },
    )
    def post(self, request: Request) -> Response:
        """
        username, paswword를 받아 유저 계정을 생성합니다.
        Args:
            username: 이름
            password: 비밀번호
        Returns:
            email: 생성된 계정 이메일
            username: 생성된 계정 이름
            code: 생성된 인증 코드
        """
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    @swagger_auto_schema(
        operation_summary="유저 로그인",
        request_body=UserLoginSerializer,
        responses={
            status.HTTP_200_OK: UserLoginSerializer,
        },
    )
    def post(self, request: Request) -> Response:
        """
        username, paswword를 받아 유저 계정을 활성화하고 JWT 토큰을 발급합니다.
        Args:
            username: 이름
            password: 비밀번호
        Returns:
            username: 이름
            token: access token과 refresh token
        """
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
