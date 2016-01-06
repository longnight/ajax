# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from models import Comment, ImagsPath
from forms import CommentForm, ImageUploadForm


def comments(request):

    form = CommentForm(request.POST or None)

    img_form = ImageUploadForm()

    if request.method == "POST" and form.is_valid():
        comment = Comment(content=form.cleaned_data.get('content'))
        if form.cleaned_data.get('quote_id'):
            comment.quote_id = form.cleaned_data.get('quote_id')

        comment.save()

        if request.is_ajax():
            print 'ajax coming~~!'
            print comment.id
            print comment.content

        print 'success!'
        return redirect('/comments/')

    comments = Comment.objects.order_by('-id').all()
    img_paths = ImagsPath.objects.order_by('-id').all()
    c = {
        'comments': comments, 'form': form, 'img_form': img_form,
        'img_paths': img_paths,
        }

    return render(request, 'comments.html', c)


def img_upload(request):
    if request.method == 'POST':
        img_form = ImageUploadForm(request.POST, request.FILES)
        if img_form.is_valid():
            img_path = ImagsPath(img=img_form.cleaned_data.get('img'))
            img_path.save()
            print 'upload success!'
            print img_path.img

        return redirect('/comments/')

