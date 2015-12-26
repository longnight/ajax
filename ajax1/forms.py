# -*- coding: utf-8 -*-
from django import forms


class CommentForm(forms.Form):

    content = forms.CharField(label='content',
                              required=True,
                              widget=forms.Textarea
                              )

    quote_id = forms.CharField(label='quote_id',
                               required=False,
                               widget=forms.TextInput,
                               )
