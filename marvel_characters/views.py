from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
import pandas

# Create your views here.
@api_view(['GET', 'POST'])
def characterprofile_details(request):
    if request.method == "GET":
        characterprofiles = CharacterProfile.objects.all()
        serializer = CharacterProfileSerializer(characterprofiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        if request.FILES:
            data_df = pandas.read_csv(request.FILES['character_data'])

            # Handle null values
            data_df['birthplace'] = data_df['birthplace'].fillna('')
            data_df['religions'] = data_df['religions'].apply(lambda x: x if x else [])  # Convert empty strings to empty lists
            data_df['gender'] = data_df['gender'].fillna('')
            data_df['occupation'] = data_df['occupation'].apply(lambda x: x if x else [])  # Convert empty strings to empty lists

            # Convert to dictionary list
            data_list = data_df.to_dict(orient='records')

            # Create and validate serializers
            serializers = [CharacterProfileSerializer(data=row) for row in data_list]
            valid_serializers = [s for s in serializers if s.is_valid(raise_exception=True)]

            if valid_serializers:
                # Save valid profiles
                for serializer in valid_serializers:
                    serializer.save()
                return Response({'Successfully Uploaded'}, status=status.HTTP_201_CREATED)
            else:
                # Handle invalid data (all serializers failed validation)
                error_messages = [s.errors for s in serializers]  # Collect errors from all serializers
                return Response({'errors': error_messages}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'No file uploaded.'}, status=status.HTTP_400_BAD_REQUEST)