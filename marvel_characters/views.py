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

            # replacing NA with an empty string
            replaceNA(data_df, ['char', 'charname', 'birthname', 'birthplace', 'religions', 'gender'])
            convert_to_list(data_df, ['types', 'universes', 'superpowers', 'occupation', 'memberof'])
            
            # Convert to dictionary list
            data_list = data_df.to_dict(orient='records')

            # Create and validate serializers
            serializer = CharacterProfileSerializer(data=data_list, many=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response('Successfully Uploaded', status=status.HTTP_201_CREATED)
        else:
            return Response({'No file uploaded.'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
def replaceNA(file_name, key_names):
    for key in key_names:
        file_name[key] = file_name[key].replace("nan", pandas.NA).fillna('')
        
        

def convert_to_list(file_name, key_names):
    for key in key_names:
        # REPLACES NAN WITH BLANK STRING. 
         file_name[key] = file_name[key].fillna('').astype(str).str.split(', ')

        