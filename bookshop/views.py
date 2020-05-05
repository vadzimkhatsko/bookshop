from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from bookshop import models
from bookshop.forms import CommentForm
from bookshop.task import test_fun

#logger = logging.getLogger('django')
promise = None
def hello(request):
    global promise
    promise = test_fun.delay(10)
    return HttpResponse('<h1> hello from django </h1>')

def index(request):
    global promise
    response = {}
    if getattr(promise, 'state', False) != "PENDING":
        respose = {'promise': promise.get()}
    response['comment'] = CommentForm()
    response['books'] = models.Book.objects.all()
    return render(request, "./bookshop/index.html", response )

def comment_handler(request, id_book):
    form = CommentForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.comment_book_id = id_book
        obj.save()
        return redirect('/django')
    return HttpResponse('error')


