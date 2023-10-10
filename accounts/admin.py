from django.contrib import admin
from .models import UserProfile,Education,Experience,CreateProfile,Login,Register

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(CreateProfile)
admin.site.register(Login)
admin.site.register(Register)