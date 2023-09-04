from django.contrib import admin
from django.urls import path
from school import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name=''),

    path('adminclick', views.adminclick_view),
    path('adminsignup', views.admin_signup_view),
    path('studentsignup1', views.student_signup_view, name='studentsignup1'),
    path('adminlogin', LoginView.as_view(template_name='school/adminlogin.html')),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='school/index.html'), name='logout'),
    path('admin-dashboard', views.admin_dashboard_view, name='admin-dashboard'),
    # path('adminlogin', views.admin_login_view,name='adminlogin'),

    # path('add/', views.person_create_view, name='person_add'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),
    path('aboutus', views.aboutus_view),

]
