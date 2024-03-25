from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def aws(request):
    return render(request,"myapp/aws.html")

def azure(request):
    return render(request,"myapp/azure.html")
	
def gcp(request):
    return render(request,"myapp/gcp.html")

def vmware(request):
    return render(request,"myapp/vmware.html")