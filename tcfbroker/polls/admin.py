from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice
from .models import Profile
from .models import Resource 
from import_export import resources
from .models import Assessment
    
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Profile)
admin.site.register(Resource) 
admin.site.register(Assessment) 