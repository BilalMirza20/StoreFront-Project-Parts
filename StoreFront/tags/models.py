from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    title = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # What tag applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE) # tag
    # To create a generic relationship we need Type and ID of an object:
    # Type (product, video, article)
    # ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) # ContentType represent the type of object of our application.
    object_id = models.PositiveIntegerField() # object ID
    content_object = GenericForeignKey() # The actual object that a particular tag is applied to.


