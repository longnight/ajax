# -*- coding: utf-8 -*-
import os
import datetime
import time
from django.db import models
from sorl.thumbnail import ImageField

class Comment(models.Model):
    content = models.TextField(blank=False)
    quote = models.ForeignKey('self',
                              null=True,
                              on_delete=models.CASCADE,
                              related_name='quoting_me_comments'
                              )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return 'comment: %s' % self.id


def user_upload_file(instance, filename):
    fileExtension = os.path.splitext(filename)[1].lower()
    head = datetime.datetime.now().strftime("%Y_%m") + "/"
    tail = str(int(time.time())) + fileExtension
    return head + tail


class ImagsPath(models.Model):
    img = ImageField(upload_to=user_upload_file)
