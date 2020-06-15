# your django admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Project, State,\
                    Transition, Workflow, Task, Checklist

class UserAdmin(BaseUserAdmin):
    
    fieldsets =  (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'profile_pic', 'phone_no',)}
        ),
    )

DataModels = [Project, State, Transition, Workflow, Task, Checklist]
admin.site.register(User, UserAdmin)
admin.site.register(DataModels)
