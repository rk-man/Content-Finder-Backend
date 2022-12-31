from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from base.models import Content, Profile
from base.serializers import ContentSerializer, ContentSubSerializer
from rest_framework.response import Response
import six
import imghdr
import base64
import uuid
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from rest_framework import serializers


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


@api_view(["GET"])
def getAllContent(req):
    content = Content.objects.all()
    # print(photoshops)
    sr = ContentSerializer(content, many=True)
    return Response(sr.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getOtherUsersContent(req):
    profile = req.user.profile
    content = Content.objects.exclude(owner=profile)
    sr = ContentSerializer(content, many=True)
    return Response(sr.data)


@api_view(["GET"])
def getContent(req, pk):
    content = Content.objects.get(id=pk)
    sr = ContentSerializer(content, many=False)
    return Response(sr.data)


@api_view(["GET"])
def getUserContent(req, pk):
    print(pk)
    profile = Profile.objects.get(id=pk)
    content = Content.objects.filter(owner=profile)
    sr = ContentSerializer(content, many=True)
    return Response(sr.data)


# create content
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createContent(req):
    data = req.data
    profile = req.user.profile

    format, imgStr = data["file"].split(';base64,')

    ext = data["ext"]

    fileName = "content-" + str(uuid.uuid4())[:15] + f".{ext}"

    contentFile = ContentFile(base64.b64decode(imgStr), name=fileName)

    imageFile = decode_base64_file(data["coverImage"])

    content = Content.objects.create(
        owner=profile,
        title=data["title"],
        category=data["category"],
        file=contentFile,
        coverImage=imageFile,
        description=data["description"],
        price=data["price"],
        fileType=data["fileType"]
    )

    sr = ContentSerializer(content, many=False)

    return Response(sr.data)


#  update content
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def updateContent(req, pk):
    content = Content.objects.get(id=pk)
    data = req.data
    content.title = data["title"]
    content.description = data["description"]
    content.category = data["category"]
    content.price = data["price"]
    content.fileType = data["fileType"]

    format, imgStr = data["file"].split(';base64,')

    ext = data["ext"]

    fileName = "content-" + str(uuid.uuid4())[:15] + f".{ext}"

    contentFile = ContentFile(base64.b64decode(imgStr), name=fileName)

    coverImage = decode_base64_file(data["coverImage"])

    content.file = contentFile
    content.coverImage = coverImage

    content.save()

    sr = ContentSerializer(content, many=False)
    return Response(sr.data)


# delete content
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deleteContent(req, pk):
    # check if the deleting content is in fact being deleted by the user
    profile = req.user.profile
    content = Content.objects.get(id=pk)
    if (content.owner.id != profile.id):
        return

    content.delete()

    data = {
        "detail": "Content deleted successfully"
    }
    return Response(data)


# get trending content
@api_view(["GET"])
def getTrendingContent(req):
    content = Content.objects.filter(trending=True)
    sr = ContentSerializer(content, many=True)
    return Response(sr.data)


# Add like or remove like to a content
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def addLikeToContent(req, pk):
    profile = req.user.profile
    content = get_object_or_404(Content, id=pk)

    # if a content already has a user, then remove the like
    if (content.likes.filter(id=profile.id)):
        content.likes.remove(profile)
    else:
        content.likes.add(profile)

    sr = ContentSerializer(content, many=False)
    return Response(sr.data)


# get user liked content
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getUserLikedContent(req):
    profile = req.user.profile
    content = Content.objects.filter(likes=profile)
    sr = ContentSubSerializer(content, many=True)
    return Response(sr.data)


@api_view(["GET"])
def getSearchResults(req, query):
    updatedQuery = query.strip()
    if (not (query and updatedQuery)):
        return Response({"content": []})

    content = Content.objects.filter(
        category__icontains=updatedQuery) or Content.objects.filter(title__icontains=updatedQuery) or Content.objects.filter(fileType__icontains=updatedQuery)

    sr = ContentSerializer(content, many=True)
    data = {
        "totalResults": content.count(),
        "content": sr.data
    }

    return Response(data)
