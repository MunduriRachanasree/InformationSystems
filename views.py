from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,render_to_response
from .forms import DriveForm
from  TPOv1.models import Drive


def index(request):
    if request.method == "POST":
        form = DriveForm(request.POST) 
        if form.is_valid():		
            Drive = form.save(commit = False)
            Drive.save()            
            return redirect('success')
        
    else:
        form = DriveForm()
    return render(request, "index.html", {'form': form})


def success(request):
			try:
				drive_details = Drive.objects.all()
			except Drive.DoesNotExist:
				raise Http404("DriveDetails does not exist")
			return render(request, 'viewDrives.html', {'drive_details': drive_details})
			
def display(request):
			try:
				Student = Drive.objects.all()
			except Drive.DoesNotExist:
				raise Http404("Comment does not exist")
			return render(request, "display.html",{'Student': Student})
