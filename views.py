from django.shortcuts import render,redirect,render_to_response
from StudentInformationSystem.forms import PersonInfoForm
from StudentInformationSystem.models import PersonalInfo
from django.http import HttpResponse,HttpResponseRedirect


def index(request):
	return HttpResponse("WELCOME TO STUDENT INFORMATION SYSTEM")


def base(request):
    if request.method == "POST":
        form = PersonInfoForm(request.POST)
        if form.is_valid():
            PersonInfo = form.save(commit=False)
            PersonInfo.save()
            return redirect('success')
    else:
        form = PersonInfoForm()
    return render(request, 'StudentInformationSystem/base.html', {'form': form})
	
def display(request):
         try:
             Student = PersonalInfo.objects.all()
         except PersonalInfo.DoesNotExist:
             raise Http404("Comment does not exist")
            
         return render(request, "StudentInformationSystem/display.html",{'Student': Student})