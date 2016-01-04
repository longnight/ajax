# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from models import Comment
from forms import CommentForm


def comments(request):

    form = CommentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():

        comment = Comment(
            content=form.cleaned_data.get('content'),
            quote_id=form.cleaned_data.get('quote_id')
            )
        comment.save()
        if request.is_ajax():
            print 'ajax coming~~!'
            print comment.id
            print comment.content

        print 'success!'
        return redirect('/comments/')

    comments = Comment.objects.order_by('-id').all()
    c = {'comments': comments, 'form': form}
    return render(request, 'comments.html', c)
