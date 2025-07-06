from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class LikedItem(models.Model):
    # what user like what object
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # To create a generic relationship we need Type and ID of an object:
    # Type (product, video, article)
    # ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) # ContentType represent the type of object of our application.
    object_id = models.PositiveIntegerField() # object ID
    content_object = GenericForeignKey() # The actual object that a particular tag is applied to.
