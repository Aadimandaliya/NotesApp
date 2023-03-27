from django.shortcuts import render,redirect
from .forms import signupform,notesform,updateform,feedbackform
from .models import usersignup,mynotes,feedback
from django.contrib.auth import logout
from django.core.mail import send_mail
from NOTESAPP import settings

# Create your views here.
 
def index(request):
    if request.method=="POST": #rooot
        if request.POST.get('signup')=='signup':
            newuser=signupform(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("signup successfully")
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':
            unm = request.POST['username']
            pas = request.POST['password']

            uid = usersignup.objects.get(username=unm)
            print("current userid: ",uid.id)
            user = usersignup.objects.filter(username=unm,password=pas)
            if user:  # true
                print('login succesfully!')
                request.session['user']=unm  #create session
                request.session['userid']=uid.id
                return redirect('notes')
                
            else:
                print("Error login failed")
    return render(request, 'index.html')

def notes(request):
    user=request.session.get('user')
    if request.method == 'POST':
        newnotes=notesform(request.POST,request.FILES)
        if newnotes.is_valid():
            newnotes.save()
            print('new notes successfully saved')
        else:
            print(newnotes.errors)
    return render(request, 'notes.html',{'user':user})

def profile(request):
    user=request.session.get('user')
    uid=request.session.get('userid')
    cuser=usersignup.objects.get(id=uid)
    if request.method == 'POST':
        updateduser=updateform(request.POST)
        if updateduser.is_valid():
            updateduser=updateform(request.POST,instance=cuser)
            updateduser.save()
            print("your data has been updated...")
        else:
            print(updateduser.errors)

    return render(request, 'profile.html',{'user':user,'cuser':usersignup.objects.get(id=uid)})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=='POST':
        fbuser = feedbackform(request.POST)
        if fbuser.is_valid():
            fbuser.save()
            print('your feedback is submitted')

            # email sending code 
            # send_mail(subject='thankyou',message=f'Dear user,/nWe got your feedback,/nThank you for your interest./nneed any help,/ncontact us +916353231368',from_email=settings.EMAIL_HOST_USER,recipient_list=['adimandaliya03@gmail.com'])

            sub='thankyou'
            msg=f"Dear user,\nWe got your feedback,\nThank you for your interest.\nneed any help,\ncontact us +916353231368"
            from_id=settings.EMAIL_HOST_USER
            to_id=[request.POST['email']]

            send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id)

        else:
            print(fbuser.errors)
    return render(request, 'contact.html')

def userlogout(request):
    logout(request)
    return redirect('/')