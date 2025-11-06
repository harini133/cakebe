from django.shortcuts import render
from cakeapp.models import cakebelogin,cakebecakes
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,"index.html")

def adminlogin(request):
    return render(request,"adminlogin.html")

def adminhome(request):
    return render(request,"dashboard.html")

def dashboard(request):
    return render(request,"dashboard.html")

def checklogin(request):
    user=request.POST["username"]
    pas=request.POST["password"]
    
    if cakebelogin.objects.filter(username=user,password=pas).exists():
        return HttpResponseRedirect("/dashboard") 
    else:
        ermsg="wrong login"
        return render(request,"login.html",{"errmsg":ermsg})
    
def addcakes(request):
    cname=request.POST["cakename"]
    ctype=request.POST["caketype"]
    cprice=request.POST["cakeprice"]
    cquantity=request.POST["cakequantity"]
    cweight=request.POST["cakeweight"]
    cphoto=request.FILES["cakephoto"]
    cake=cakebecakes()
    cake.cakename=cname
    cake.caketype=ctype
    cake.cakeprice=cprice
    cake.cakequantity=cquantity
    cake.cakeweight=cweight
    cake.cakephoto=cphoto
    cake.save()
    res="data successfully addde"
    return render(request,"addcakes.html",{"result":res})

def addproducts(request):
    return render(request,"addcakes.html")

def viewall(request):
    res=cakebecakes.objects.all()
    return render(request,"viewall.html",{"result":res})

def selectcake(request,id):
    res=cakebecakes.objects.get(id=id)
    return render(request,"selectcake.html",{"result":res})

def deletecake(request,id):
    res=cakebecakes.objects.get(id=id)
    res.delete()
    return HttpResponseRedirect("/viewall")

def modifycake(request,id):
    res=cakebecakes.objects.get(id=id)
    return render(request,"updatecake.html",{"result":res})

def updatecakes(request,id):
    cname=request.POST["cakename"]
    ctype=request.POST["caketype"]
    cprice=request.POST["cakeprice"]
    cquantity=request.POST["cakequantity"]
    cweight=request.POST["cakeweight"]
    cphoto=request.FILES["cakephoto"]
    cake=cakebecakes.objects.get(id=id)
    cake.cakename=cname
    cake.caketype=ctype
    cake.cakeprice=cprice
    cake.cakequantity=cquantity
    cake.cakeweight=cweight
    cake.cakephoto=cphoto
    cake.save()
    return HttpResponseRedirect("/viewall")

def cakebehome(request):
    return render(request,"index.html")