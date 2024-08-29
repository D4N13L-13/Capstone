from django.contrib import admin
from .models import Question, Choice

# Register your models here.
# Registering the `Question` and `Choice`
# Managed and viewed through the Django admin site.
# Once registered, you can access and interact with instances of these
# models through the admin interface
admin.site.register(Question)
admin.site.register(Choice)
