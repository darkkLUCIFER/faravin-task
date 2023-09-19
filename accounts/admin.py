from django.contrib import admin
from accounts.models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    class Meta:
        model = Users
        fields = '__all__'
