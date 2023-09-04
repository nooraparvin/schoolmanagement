from django.shortcuts import render, redirect, reverse
from . import forms, models
from .models import UserOrder, Course, Department
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UserOrderForm, AdminSignupForm
from django.http import JsonResponse


def home_view(request):
    return render(request, 'school/index.html')


def adminclick_view(request):
    return render(request, 'school/adminclick.html')


def studentclick_view(request):
    return render(request, 'school/studentclick.html')


def admin_signup_view(request):
    form = forms.AdminSignupForm()
    if request.method == 'POST':
        form = forms.AdminSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('adminlogin')
    return render(request, 'school/adminsignup.html', {'form': form})


def student_signup_view(request):
    departments = Department.objects.all()
    purposes = ["Enquiry", "Place Order", "Return"]
    if request.method == 'POST':
        message = "Form submitted successfully."
        # return render(request, 'school/studentsignup1.html', {'message': message})
        redirect_link = "/"
        return render(request, 'school/studentsignup1.html', {'message': message, 'redirect_link': redirect_link})
    return render(request, 'school/studentsignup1.html', {
        'departments': departments,
        'purposes': purposes,
    })

    # message = "Successfully Done"
    #  return render(request, 'school/studentsignup1.html', {'message': message})


def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()


def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')
    return render(request, 'school/admin_dashboard.html')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    return render(request, 'school/admin_dashboard.html')


def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    course_data = [{'id': course.id, 'name': course.name} for course in courses]
    return render(request, 'school/form.html', {'courses': courses})
    # return JsonResponse({'courses': course_data})


def aboutus_view(request):
    return render(request, 'school/aboutus.html')
