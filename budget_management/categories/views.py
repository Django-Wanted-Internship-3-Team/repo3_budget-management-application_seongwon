from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from budget_management.categories.models import Category
from budget_management.categories.serializers import CategorySerializer


class CategoryListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="카테고리 목록 조회",
        responses={
            status.HTTP_200_OK: CategorySerializer,
        },
    )
    def get(self, request: Request) -> Response:
        """
        전체 카테고리 목록을 조회합니다.
        Args:

        Returns:
            categories: 카테고리 리스트
        """
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
