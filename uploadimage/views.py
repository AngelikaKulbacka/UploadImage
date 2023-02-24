from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Image
from django.contrib.auth.models import User
from Project.serializers import ImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class ImageList(APIView):
    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

class ImageUpload(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        # Get the user's plan and check permissions
        user_plan = User.groups
        if user_plan == 'Basic':
            # Handle Basic plan permissions
            return Response({'message': 'You do not have permission to upload images.'},status=status.HTTP_403_FORBIDDEN)
        elif user_plan == 'Premium':
            # Handle Premium plan permissions
            thumbnail_sizes = [200, 400]
            serializer = ImageSerializer(data=request.data, context={'request': request, 'thumbnail_sizes': thumbnail_sizes})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif user_plan == 'Enterprise':
            # Handle Enterprise plan permissions
            thumbnail_sizes = [200, 400]
            serializer = ImageSerializer(data=request.data, context={'request': request, 'thumbnail_sizes': thumbnail_sizes})
            if serializer.is_valid():
                serializer.save()
                # Generate an expiring link and add it to the response
                image = serializer.instance
                expiring_link = image.generate_expiring_link(300)
                serializer_data = serializer.data
                serializer_data['expiring_link'] = expiring_link
                return Response(serializer_data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Handle unknown plan types
            return Response({'message': 'Unknown account type.'}, status=status.HTTP_403_FORBIDDEN)

class ImageDetail(APIView):
    def get_object(self, pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        image = self.get_object(pk)
        serializer = ImageSerializer(image)
        return Response(serializer.data)

    def put(self, request, pk):
        image = self.get_object(pk)
        serializer = ImageSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        image = self.get_object(pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ImageLink(APIView):
    def get(self, request, pk):
        # Get the image and check permissions
        image = Image.objects.get(pk=pk)
        if image.user != request.user:
            return Response({'message': 'You do not have permission to access this image.'},
                            status=status.HTTP_403_FORBIDDEN)
        user_plan = request.user.userprofile.plan
        if user_plan != 'Enterprise':
            return Response({'message': 'You do not have permission to generate expiring links.'},
                            status=status.HTTP_403_FORBIDDEN)
        # Generate an expiring link and return it in the response
        seconds = int(request.GET.get('seconds', 300))
        expiring_link = image.generate_expiring_link(seconds)
        return Response({'expiring_link': expiring_link})
