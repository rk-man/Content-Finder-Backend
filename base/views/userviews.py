from base.models import Profile
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from base.serializers import ProfileSerializer
from rest_framework.response import Response

import six
import imghdr
import base64
import uuid
from django.core.files.base import ContentFile


def decode_base64_file(data):
    def get_file_extension(file_name, decoded_file):

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

    # Check if this is a base64 string
    if isinstance(data, six.string_types):
        # Check if the base64 string is in the "data:" format
        if 'data:' in data and ';base64,' in data:
            # Break out the header from the base64 content
            header, data = data.split(';base64,')

        # Try to decode the file. Return validation error if it fails.
        try:
            decoded_file = base64.b64decode(data)
        except TypeError:
            TypeError('invalid_image')

        # Generate file name:
        # 12 characters are more than enough.
        file_name = "cover-image" + str(uuid.uuid4())[:12]
        # Get the file name extension:
        file_extension = get_file_extension(file_name, decoded_file)

        complete_file_name = "%s.%s" % (file_name, file_extension, )

        return ContentFile(decoded_file, name=complete_file_name)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def updateUserProfile(req, pk):
    # print(req.data)
    updatedProfile = Profile.objects.get(id=pk)
    updatedProfile.name = req.data["name"]
    updatedProfile.username = req.data["username"]
    updatedProfile.email = req.data["email"]
    updatedProfile.short_description = req.data["shortDescription"]
    updatedProfile.country = req.data["country"]
    updatedProfile.bio = req.data["bio"]

    pImage = decode_base64_file(req.data["profileImage"])
    updatedProfile.profileImage = pImage

    updatedProfile.save()

    sr = ProfileSerializer(updatedProfile, many=False)
    return Response(sr.data)


@api_view(["GET"])
def getAllProfiles(req):
    profiles = Profile.objects.all()
    sr = ProfileSerializer(profiles, many=True)
    return Response(sr.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getOtherProfiles(req):
    user = req.user
    profiles = Profile.objects.exclude(user=user)
    sr = ProfileSerializer(profiles, many=True)
    return Response(sr.data)


@api_view(["GET"])
def getProfile(req, pk):
    profile = Profile.objects.get(id=pk)
    sr = ProfileSerializer(profile, many=False)
    return Response(sr.data)


@api_view(["GET"])
def searchUsers(req, query):
    updatedQuery = query.strip()
    if (not (query and updatedQuery)):
        return Response({"profiles": []})

    profiles = Profile.objects.filter(
        name__icontains=updatedQuery) or Profile.objects.filter(short_description__icontains=updatedQuery) or Profile.objects.filter(username__icontains=updatedQuery)

    sr = ProfileSerializer(profiles, many=True)
    data = {
        "totalResults": profiles.count(),
        "profiles": sr.data
    }

    return Response(data)
