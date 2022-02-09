from urllib import response
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, redirect

from myproject.settings import SECRET_KEY
from .models import Branch, Loanform
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
import json
import requests
# Create your views here.


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def members(request):

    branch_files = Branch.objects.values_list('bname').distinct()

    context = {"branch_files": branch_files}
    return render(request, 'members.html', context)


def articles(request):
    return render(request, 'articles.html')


def loan(request):
    if request.method == 'POST':
        name = request.POST['name']
        phno = request.POST['phno']
        regno = request.POST['regno']
        # userform = request.POST['userform']
        # userform = request.FILES.getlist('userform')

        clientKey = request.POST['g-recaptcha-response']
        secretKey = '6LeR-WgeAAAAACqn_XhFpkd80BMRqn1gJqHSFCVq'
        captchaData = {'secret': secretKey, 'response': clientKey}
        req = requests.post(
            'https://www.google.com/recaptcha/api/siteverify', data=captchaData)

        response = json.loads(req.text)
        verify = response['success']
        if verify:
            files = request.FILES.getlist('userform')
            for file in files:
                Loanform(name=name, phno=phno,
                         regno=regno, userform=file).save()
            messages.success(
                request, "your form have been submitted successfully")
        else:
            messages.error(
                request, "Please verify recaptcha")
        return render(request, 'loan.html')
    return render(request, 'loan.html')


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
    if request.method == "POST":
        name = request.POST['bname']
        files = request.FILES.getlist('bfile')
        for file in files:
            Branch(bname=name, bfiles=file).save()
        messages.success(request, 'Your files has been uploaded successfully')
        return HttpResponseRedirect("/members")
    userforms = Loanform.objects.all().order_by('-id')
    context = {"userforms": userforms}
    return render(request, 'admin.html', context)


def deleteform(request, id):
    if request.method=="POST":
        pi = Loanform.objects.get(id=id)
        pi.delete()
        # return render(request, "admin.html")
        return HttpResponseRedirect("/adminpanel")
    return render(request,"admin.html")
