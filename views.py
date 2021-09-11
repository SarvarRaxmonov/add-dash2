from django.shortcuts import redirect, render
from .models import Mentor, Groupv
from .forms import MentorCreateForm, GroupCreateForm, createuserform
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only



        

@unauthenticated_user
def registerPage(request):

	form = createuserform()
	if request.method == 'POST':
		form = createuserform(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='customer')
			user.groups.add(group)
			#Added username after video because of error returning customer name if not added
		    #     customer.objects.create(
			# 	      user=user,


			# 	      name=user.username,
			# 	)

			# messages.success(request, 'Account was created for ' + username)

		return redirect('log')
		

	context = {'form':form}
	return render(request, 'mainapp/reg.html', context)


@unauthenticated_user


def loginPage(request):
    
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('dashboard')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'mainapp/log.html', context)























def logoutuser(request):
    logout(request)
    return redirect('log')





















@login_required(login_url='log')
@allowed_users(allowed_roles=['customer', 'admin'])
def dashboard(request):
    return render(request, "mainapp/index.html")


# def add_mentor(request):
#     if request.method == 'POST':
#         form = MentorRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#     else:
#         form = MentorRegistrationForm()

#     context = {
#         'form': form
#     }

#     return render(request, "dashboardapp/add_mentor.html", context)


@login_required(login_url='log')
@allowed_users(allowed_roles=['admin'])
def createMentor(request):
    form = MentorCreateForm()
    if request.method == "POST":
        form = MentorCreateForm(request.POST)
        if form.is_valid:
            form.save()
        
            return redirect("mentors_table")


    else:
        form = MentorCreateForm()

    context = {
        "form" : form
    }
    return render(request, "mainapp/create_mentor.html", context)


@login_required(login_url='log') 
@allowed_users(allowed_roles=['admin'])  
def updateMentor(request, pk):
    mentor = Mentor.objects.get(id=pk)
    form  = MentorCreateForm(instance=mentor)
    if request.method == "POST":
        form = MentorCreateForm(request.POST, instance=mentor)
        if form.is_valid:
            form.save()
            return redirect("mentors_table")

    
    context = {
        "form" : form
    }

    return render(request, "mainapp/create_mentor.html", context)


@login_required(login_url='log')
@allowed_users(allowed_roles=['admin'])
def deleteMentor(request, pk):
    mentor = Mentor.objects.get(id=pk)
    if request.method == "POST":
        mentor.delete()
        return redirect('mentors_table') 
    context = {
        'mentor': mentor
    }
    return render(request, 'mainapp/delete_mentor.html', context)


@login_required(login_url='log')
@allowed_users(allowed_roles=['customer', 'admin'])
def mentorsTable(request):
    mentors = Mentor.objects.all()

    context = {
        "mentors": mentors
    }
    return render(request, "mainapp/mentors_table.html", context)




@login_required(login_url='log')
@allowed_users(allowed_roles=['customer', 'admin'])
def groupsTable(request):
    groups = Groupv.objects.all()
    context = {
        "groups": groups 
    }
    return render(request, "mainapp/groups_table.html", context)


@login_required(login_url='log')
@allowed_users(allowed_roles=['admin'])
def createGroup(request):
    form = GroupCreateForm()
    if request.method == "POST":
        form = GroupCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("groups_table")
    
    else:
        form = GroupCreateForm()
  
    context = {
        "form" : form
    }
    return render(request, "mainapp/create_group.html", context)


@login_required(login_url='log')
@allowed_users(allowed_roles=['admin'])
def updateGroup(request, pk):
    group = Group.objects.get(id=pk)
    form  = GroupCreateForm(instance=group)
    if request.method == "POST":
        form = GroupCreateForm(request.POST, instance=group)
        if form.is_valid:
            form.save()
            return redirect('groups_table')

    context = {
        "form" : form
    }

    return render(request, "mainapp/create_group.html", context)




@login_required(login_url='log')
@allowed_users(allowed_roles=['admin'])
def deleteGroup(request, pk):
    group = Group.objects.get(id=pk)
    if request.method == "POST":
        group.delete()
        return redirect('groups_table') 
    context = {
        'group': group
    }
    return render(request, 'mainapp/delete_group.html', context)


