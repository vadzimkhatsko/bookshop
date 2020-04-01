from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from bookshop import models
from bookshop.forms import CommentForm

def index(request):
    book = models.Book.objects.all()
    response = {}
    response['comment'] = CommentForm()
    return render(request, "index.html", {"books": book}, response )

def comment_handler(request, id_book):
    form = CommentForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.comment_book_id = id_book
        obj.save()
        return redirect('/')
    return HttpResponse('error')

def hello(request):
    return HttpResponse('<h2> Hello  from django</h2>')

def world(request):
    response = {}
    response['name']= "Egor"
    response['users']= ["pavel", "evgen", "godjima", "gaben"]
    return render(request, './bookshop/index.html', response)
