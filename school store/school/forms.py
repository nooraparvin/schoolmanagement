from django import forms
from django.contrib.auth.models import User
from . import models
from .models import UserOrder


# for admin
class AdminSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class UserOrderForm(forms.ModelForm):
    class Meta:
        model = UserOrder
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['course'].queryset = Course.objects.none()
    #
    #     if 'department' in self.data:
    #         try:
    #             department_id = int(self.data.get('department'))
    #             self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
    #         except (ValueError, TypeError):
    #             pass
    #     elif self.instance.pk:
    #         self.fields['course'].queryset = self.instance.department.course_set.order_by('name')
