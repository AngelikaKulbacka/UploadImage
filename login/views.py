from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.
class LoginAPIView(APIView):

    def post(self, request):

        username = request.data.get('username', None)
        password = request.data.get('password', None)

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'Message': 'Logged In'}, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'Invalid username and password combination'},
                            status=status.HTTP_401_UNAUTHORIZED)