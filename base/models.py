
from django.db.models.signals import post_save, pre_save
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.dispatch import receiver
from django.utils import timezone
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    profileImage = models.ImageField(
        default="images/user-profiles/default-profile.png", upload_to="images/user-profiles/")
    # profileImage = models.ImageField(
    #     upload_to="images/user-profiles/", null=True, blank=True)

    short_description = models.CharField(max_length=300, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    country = models.CharField(
        max_length=200, null=True, blank=True)
    createdAt = models.DateTimeField(default=timezone.now, blank=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.username


class Content(models.Model):

    FILE_TYPES = (
        (".psd (photoshop)", ".psd (photoshop)"),
        (".ai (illustrator)", ".ai (illustrator)"),
        (".fig (figma)", ".fig (figma)"),
        (".zip (zip file)", ".zip (zip file)"),
        (".aep (after effects)", ".aep (after effects)"),
        ("stock photos", "stock photos"),
        ("others", "others")
    )

    CATEGORIES = (
        ("advertisement", "advertisement"),
        ("resume", "resume"),
        ("youtube", "youTube"),
        ("websites", "websites"),
        ("instagram", "instagram"),
        ("facebook", "facebook"),
        ("others", "others"),
    )

    title = models.CharField(max_length=300, null=True, blank=True)
    category = models.CharField(
        max_length=200, null=True, blank=True, choices=CATEGORIES)
    file = models.FileField(
        null=True, blank=True, upload_to="files/")
    coverImage = models.ImageField(
        null=True, blank=True, upload_to="images/cover-images/")
    description = models.TextField(
        max_length=4000, default="", null=True, blank=True)
    price = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=2)
    owner = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    fileType = models.CharField(max_length=200, choices=FILE_TYPES)

    likes = models.ManyToManyField(
        Profile, blank=True, related_name="content_like")

    trending = models.BooleanField(default=False, blank=True, null=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Order(models.Model):
    STATUS_CHOICES = (
        ('In progress', 'In progress'),
        ('Successfull', 'Successfull'),
        ('Failed', 'Failed')
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    buyer = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    orderItems = models.ManyToManyField(
        Content, blank=True, related_name="order_items")
    totalPrice = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=2)
    orderedAt = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(
        max_length=200, null=True, blank=True, choices=STATUS_CHOICES, default="In progress")


@receiver(post_save, sender=Profile)
def updateUser(sender, instance, created, **kwargs):

    if (not created):
        user = instance.user
        name = instance.name.split(" ")

        if (len(name) >= 2):
            first_name = name[0]
            last_name = name[1]
        else:
            first_name = name
            last_name = ""

        try:
            user.first_name = first_name
            user.last_name = last_name
            user.username = instance.username
            user.email = instance.email

            user.save()
        except:
            print("Some error occured")
    else:
        pass


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if (created):
        print(instance)
        print("user created")
        Profile.objects.create(
            username=instance.username,
            email=instance.email,
            user=instance
        )
    else:
        pass
