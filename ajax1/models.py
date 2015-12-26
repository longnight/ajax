# -*- coding: utf-8 -*-
from django.db import models


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
