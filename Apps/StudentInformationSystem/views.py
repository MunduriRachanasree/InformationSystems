from django.shortcuts import render,redirect
from StudentInformationSystem.forms import *
from StudentInformationSystem.models import *
from django.http import HttpResponse,HttpResponseRedirect

def index(request):
	return render(request, 'StudentInformationSystem/index.html')


def base(request):
	if request.method == "POST":
		form = PersonalInfoForm(request.POST)
		if form.is_valid():
			PersonInfo = form.save(commit=False)
			PersonInfo.save()
			return HttpResponseRedirect('/StudentInformationSystem/acedamicInfo')
	else:
		form = PersonalInfoForm()
	return render(request, 'StudentInformationSystem/base.html', {'form': form})

def success(request):
	return HttpResponse("Successfully updated")
	
def acedamicInfo(request):
	if request.method == "POST":
		form = AcedamicInfoForm(request.POST)
		if form.is_valid():
			AIF = form.save(commit=False)
			try:
				Student = PersonalInfo.objects.get(pk = 32)
			except PersonalInfo.DoesNotExist:
				raise Http404("Comment does not exist")
			AIF.studentId = Student
			AIF.save()
			return HttpResponseRedirect('/StudentInformationSystem/additionalInfo')
	else:
		form = AcedamicInfoForm()
	return render(request, 'StudentInformationSystem/success.html', {'form': form})

def additionalInfo(request):
	if request.method == "POST":
		form = AdditionalInfoForm(request.POST)
		if form.is_valid():
			ADIF = form.save(commit=False)
			try:
				Student = PersonalInfo.objects.get(pk = 32)
			except PersonalInfo.DoesNotExist:
				raise Http404("Comment does not exist")
			ADIF.studentId = Student
			ADIF.save()
			return redirect('/StudentInformationSystem/home')
	else:
		form = AdditionalInfoForm()
	return render(request, 'StudentInformationSystem/additionalInfo.html', {'form': form})

def notifications(request):
	Student = PersonalInfo.objects.get(pk = 32)
	sug = Suggestion.objects.filter(studentId = Student)
	notice = Notifications.objects.all()
	return render(request, 'StudentInformationSystem/notifications.html', {'sugs': sug,'notices':notice})
	
def resume(request):
	Student = PersonalInfo.objects.get(pk = 32)
	Acedamic = AcedamicInfo.objects.get(studentId = Student)
	Additional = AdditionalInfo.objects.get(studentId = Student)
	return render(request, 'StudentInformationSystem/resume.html', {'p': Student,'ac':Acedamic,'ad':Additional})
		
def viewStudent(request):
	Student = PersonalInfo.objects.get(pk = 32)
	Acedamic = AcedamicInfo.objects.get(studentId = Student)
	Additional = AdditionalInfo.objects.get(studentId = Student)
	return render(request, 'StudentInformationSystem/StudentView.html', {'person': Student,'acedamic':Acedamic,'additional':Additional})
	
def editStudent(request):
	Student = PersonalInfo.objects.get(pk = 32)
	Acedamic = AcedamicInfo.objects.get(studentId = Student)
	Additional = AdditionalInfo.objects.get(studentId = Student)
	return render(request, 'StudentInformationSystem/EditProfile.html', {'person': Student,'acedamic':Acedamic,'additional':Additional})
	
def edit(request):
	if request.method == "POST":
		p = PersonalInfo.objects.get(id = 32);
		p.first_name = request.POST['fname']
		p.last_name = request.POST['lname']
		p.address = request.POST['address']
		p.email = request.POST['email']
		p.phoneNo = request.POST['phoneno']
		p.save()
		q = AcedamicInfo.objects.get(studentId = p)
		q.yearOfJoining = request.POST['yoj']
		q.aggregate = request.POST['aggregate']
		q.upperSecondaryInstitution = request.POST['ui']
		q.upperSecondaryBoard = request.POST['ub']
		q.upperSecondaryPercentage = request.POST['up']
		q.SecondaryInstitution = request.POST['si']
		q.SecondaryPercentage = request.POST['sp']
		q.SecondaryBoard = request.POST['sb']
		q.save()
		r = AdditionalInfo.objects.get(studentId = p)
		r.coAcademicActivities = request.POST['caa']
		r.details = request.POST['details']
		r.coCurriculars = request.POST['cca']
		r.hobbies = request.POST['hobbies']
		r.save()
		
		return render(request, 'StudentInformationSystem/index.html')
