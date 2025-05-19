from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class LogoutView(APIView):
    """Refresh tokenni blacklistga joylab, foydalanuvchini tizimdan chiqarish"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh')

        if not refresh_token:
            return Response({"error": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ProtectedView(APIView):
    """Faqat autentifikatsiya qilingan foydalanuvchilar kirishi mumkin bo'lgan view"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({
            "message": f"Hello, {request.user.username}! You are authenticated."
        }, status=status.HTTP_200_OK)