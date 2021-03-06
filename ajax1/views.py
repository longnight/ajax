# -*- coding: utf-8 -*-
# import json
import string
import random
from time import sleep
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.conf import settings
from models import Comment, ImagsPath
from forms import CommentForm, ImageUploadForm


def bootstrap(request):

    return render(request, 'bootstrap.html', {})


def comments(request):

    form = CommentForm(request.POST or None)

    img_form = ImageUploadForm()
    if request.method == "POST" and form.is_valid():
        comment = Comment(content=form.cleaned_data.get('content'))
        if form.cleaned_data.get('quote_id'):
            comment.quote_id = form.cleaned_data.get('quote_id')

        if request.is_ajax():
            print 'ajax coming~~!'
            print comment.id
            print comment.content
            comment.content += ' (from ajax!)'

        comment.save()
        print 'success!'
        return redirect('/comments/')

    comments = Comment.objects.order_by('-id').all()[:8]
    img_paths = ImagsPath.objects.order_by('-id').all()[:5]
    c = {
        'comments': comments, 'form': form, 'img_form': img_form,
        'img_paths': img_paths,
        }

    return render(request, 'comments.html', c)


def gen_random_char(size=10, flag='digits'):

    if flag == 'digits':
        charsets = '123456789'  # nonzero
    elif flag == 'lowercase':
        charsets = string.ascii_lowercase
    elif flag == 'uppercase':
        charsets = string.ascii_uppercase
    else:  # flag='any other value'
        charsets = '123456789' + string.ascii_lowercase
    rand_char = ''.join(random.SystemRandom().choice(
        charsets) for _ in range(size))
    return unicode(rand_char)


def s(request):
    s = gen_random_char(size=3)
    if request.is_ajax():
        s += '  is ajax request!'
    # sleep(2)
    return HttpResponse(s)


def img_upload(request):
    if request.method == 'POST':
        img_form = ImageUploadForm(request.POST, request.FILES)
        if img_form.is_valid():
            img_path = ImagsPath(img=img_form.cleaned_data.get('img'))
            img_path.save()
            # location = img_path.img.url
            location = 'http://' + request.get_host() + img_path.img.url
            # rv = {'location': location}
            # print rv
            status = 200
            print location
            # import pdb;pdb.set_trace()
            script_string = """
            <script>top.$('.mce-btn.mce-open').parent().find('.mce-textbox').val('%s').closest('.mce-window').find('.mce-primary').click();</script>
            """ % location
            sleep(3)
            return HttpResponse(script_string,
                                status=status
                                )
        else:
            rv = img_form.errors
            print rv
            status = 409
            return HttpResponse(
                "<script>alert('%s');</script>" % img_form.errors,
                status=status
                )
