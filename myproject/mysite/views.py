from urllib import response
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.template import RequestContext

from .models import Branch, Contact, Loanform
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
import json
import requests

from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
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
    if request.method == 'POST':
        name = request.POST['name']
        phno = request.POST['phno']
        textmsg = request.POST['textmsg']
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
           
            Contact(name=name, phno=phno,
                         message=textmsg).save()
            messages.success(
                request, "Your query have been posted successfully")
        else:
            messages.error(
                request, "Please verify recaptcha")
        return render(request, 'contact.html')
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
        # print(dictt)
        # for key, values in dictt.items():
        #     for i in values:
                # print(i)

        context = {"dictt": dictt, "branch": branchwise}
    return render(request, 'branchfiles.html', context)


def deletefile(request, branch, filename):
    if request.method == "POST":
        pi = Branch.objects.get(bfiles=filename)
        pi.delete()
        return HttpResponseRedirect("/members")


def adminpanel(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST['bname']
            files = request.FILES.getlist('bfile')
            for file in files:
                Branch(bname=name, bfiles=file).save()
            messages.success(request, 'Your files has been uploaded successfully')
            return HttpResponseRedirect("/members")
        userforms = Loanform.objects.all().order_by('-id')
        usercontact=Contact.objects.all().order_by('-id')
        context = {"userforms": userforms,'usercontacts':usercontact}
        return render(request, 'admin.html', context)
    else:
        return HttpResponseRedirect('/login')

def deleteform(request, id):
    if request.method=="POST":
        pi = Loanform.objects.get(id=id)
        pi.delete()
        # return render(request, "admin.html")
        return HttpResponseRedirect("/adminpanel")
    return render(request,"admin.html")
def deletecontact(request, id):
    if request.method=="POST":
        pi = Contact.objects.get(id=id)
        pi.delete()
        # return render(request, "admin.html")
        return HttpResponseRedirect("/adminpanel")
    return render(request,"admin.html")

def formstatus(request,id):
    pp=Loanform.objects.get(id=id)
    ppsts=pp.status
    # print(ppsts)
    if request.method=="POST":
        pi=Loanform.objects.get(id=id)
        if(ppsts):
            pi.status='False'
            # print(pi.name," ",pi.status)
            pp.status='False'
        else:
            pi.status='True'
            # print(pi.name," ",pi.status)
            pp.status='True'
        # Loanform(status=sts).save()
        # print(pi.name," ",pi.status)
        pp.save()
        return HttpResponseRedirect("/adminpanel")
    return render(request,"admin.html")



# def signup(request):
#     if request.method=="POST":
#         fm=SignUpForm(request.POST)
#         if fm.is_valid():
#             messages.success(request,'Account has been created successfull')
#             fm.save()

#     else:
#         fm=SignUpForm()
#     return render(request,'signup.html',{'form':fm})

def user_login(request):
    if not  request.user.is_authenticated:
        if request.method=='POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']

                clientKey = request.POST['g-recaptcha-response']
                secretKey = '6LeR-WgeAAAAACqn_XhFpkd80BMRqn1gJqHSFCVq'
                captchaData = {'secret': secretKey, 'response': clientKey}
                req = requests.post(
                    'https://www.google.com/recaptcha/api/siteverify', data=captchaData)

                response = json.loads(req.text)
                verify = response['success']
                if verify:
                    user=authenticate(username=uname,password=upass)
                    if user is not None:
                        login(request,user)
                        messages.success(request,"Login Successfully ")
                        return HttpResponseRedirect('/adminpanel')
                else:
                    messages.error(
                        request, "Please verify recaptcha")
                return render(request, 'login.html')
                
        else:
            fm=AuthenticationForm()
        return render(request,'login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/adminpanel')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


