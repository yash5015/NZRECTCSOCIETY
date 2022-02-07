from urllib import response
from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Branch
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def members(request):
    if request.method == "POST":
        name = request.POST['bname']
        files = request.FILES.getlist('bfile')
        for file in files:
            Branch(bname=name, bfiles=file).save()

    branch_files = Branch.objects.values_list('bname').distinct()

    context = {"branch_files": branch_files}
    return render(request, 'members.html', context)


def articles(request):
    return render(request, 'articles.html')


def contact(request):
    return render(request, 'contact.html')


def branchfiles(request, branchwise):
    if branchwise:
        listt = Branch.objects.values_list('bname', 'bfiles')
        dictt = {}
        dict_list = []
        for i in listt:
            if branchwise in i:
                dict_list.append(i[1])
        dictt[branchwise] = dict_list
        print(dictt)
        for key, values in dictt.items():
            for i in values:
                print(i)

        context = {"dictt": dictt, "branch": branchwise}
    return render(request, 'branchfiles.html', context)


def deletefile(request, branch, filename):
    if request.method == "POST":
        pi = Branch.objects.get(bfiles=filename)
        pi.delete()
        return HttpResponseRedirect("/members")


def adminpanel(request):
    return render(request, 'admin.html')
