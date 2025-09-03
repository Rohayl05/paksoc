# Django equivalent of your Java AuthController
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def hello(request):
    """Django equivalent of your HelloController.hello()"""
    return Response({"message": "Hello, World!"})

@api_view(['GET'])
@permission_classes([AllowAny])
def about(request):
    """Django equivalent of your HelloController.about()"""
    return Response({"message": "This is the about page."})

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """Django equivalent of your AuthController.register()"""
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        
        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'user_id': str(user.id),
            'email': user.email,
            'token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'role': user.role
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """Django equivalent of your AuthController.login()"""
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        
        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'user_id': str(user.id),
            'email': user.email,
            'token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'role': user.role
        })
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
