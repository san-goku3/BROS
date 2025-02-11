from django.shortcuts import render,redirect
from django.http import HttpResponse,request 

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth

#import mysql.connector 
from pg1.models import pro

# Create your views here.

def l(request):
    return render(request,'pg1.html') #home page

#for signup   
def sp(request):
    if request.method=='POST':
        
        '''m=mysql.connector.connect(host="localhost",user="root",passwd="Tanay@sql",database="reg2")
        cur=m.cursor()
'''
        for key,value in request.POST.items():
            if key=="uname":             #fetching input details
                un=value
            if key=="p1":
                ps=value     #now not storing password 
            if key=="fname":
                fn=value
            if key=="lname":
                ln=value
            if key=="nb":
                nb=value

        '''
        c="insert into signin (us,fn,ln,cn) values (%s,%s,%s,%s)"
        v=[(un,fn,ln,nb)]    #many values can be passed in dict
        cur.executemany(c,v)  
        m.commit()
        '''



        #################### NEW PART FOR LOGIN

        user=User.objects.create_user(username=un,first_name=fn,last_name=ln,password=ps)
        user.save()
        return redirect('p')   #name of func with login i.e 'p'

    return render(request,'sup2.html') #for registration

#for login
def p(request):
    if request.method=='POST':
        '''
        m=mysql.connector.connect(user='root',passwd='Tanay@sql',database='reg2',host='localhost')
        cur=m.cursor()
        '''
        un=request.POST['uname']
        ps=request.POST['psw']

        user=auth.authenticate(request,username=un,password=ps)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return HttpResponse('Wrong credentials')
    return render(request,'login.html') #for login

#for searching the data
def sr(request):
    # Check if the 'pic' parameter is provided in the GET request
    if 'pic' in request.GET:
        try:
            # Get the 'pic' value from the GET request and convert it to an integer
            pi = int(request.GET['pic'])
            # Filter records based on the 'pic' value
            e = pro.objects.filter(pic=pi)
            # Return the filtered data to the template
            return render(request, 'res.html', {'ds': e})
        except ValueError:
            # Handle the case where 'pic' is not a valid integer
            return render(request, 'search2.html', {'error': 'Invalid pin code format.'})
    else:
        # If 'pic' is not in the GET request, render the search page with no results
        return render(request, 'search2.html')


# Logout view
def lt(request):
    logout(request)  # This will log out the user
    return redirect('home')  # Redirect to the homepage or any other page

#prop view
def pr(request):
    if request.method=="POST":
        us=request.POST['us']
        pic=request.POST['pic']
        pp=request.POST['pp']
        clg=request.POST['clg']
        rt=request.POST['rt']

        pro.objects.create(us=us,pic=pic,pp=pp,clg=clg,rt=rt)
        return redirect('home')
    return render(request,"prop.html")