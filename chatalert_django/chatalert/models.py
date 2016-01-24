from django.db import models


class Message(models.Model):

    LABEL_NO_LABEL = -1
    LABEL_NO_INTEREST = 0
    LABEL_INTEREST = 1
    LABEL_CRITICAL = 2

    LABEL_CHOICES = [(LABEL_NO_LABEL, "No Label"),
                     (LABEL_NO_INTEREST, "Review"),
                     (LABEL_INTEREST, "LE Interest"),
                     (LABEL_CRITICAL, "Urgent!")]

    guid = models.TextField(unique=True)
    creation_datetime = models.DateTimeField(null=True, blank=True)
    message_type = models.TextField(blank=True)
    source = models.TextField(blank=True)
    url = models.TextField(blank=True)
    text = models.TextField(blank=True)
    author = models.TextField(blank=True)
    author_age = models.IntegerField(null=True, blank=True)
    city_state = models.TextField(blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    phone_number = models.TextField(blank=True)
    post_id = models.TextField(blank=True)
    # What do we do about timezone fields?
    comments = models.TextField(blank=True)

    label_auto = models.IntegerField(choices=LABEL_CHOICES,
                                     default=LABEL_NO_LABEL)
    label_user = models.IntegerField(choices=LABEL_CHOICES,
                                     default=LABEL_NO_LABEL)
