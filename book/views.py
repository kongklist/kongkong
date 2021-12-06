from django.shortcuts import redirect, render
from .models import Book

# Create your views here.

def index(request):
    b = request.user.book_set.all()
    context = {
        "blist" : b
    }
    return render(request, "book/index.html", context)

def create(request):
    if request.POST.get("sname"):
        sn = request.POST.get("sname")
        su = request.POST.get("surl")
        co = request.POST.get("comment")
        im = request.POST.get("impo")
        if im:
            im = True
        else:
            im = False
        Book(user=request.user, site_name=sn, site_url=su, comment=co, impo=im).save()
        return redirect("book:index")
    return render(request, "book/create.html")

def delete(request, bpk):
    Book.objects.get(id=bpk).delete()
    return redirect("book:index")
    