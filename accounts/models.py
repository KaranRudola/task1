from django.db import models

class SysUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    employee_number = models.CharField(max_length=20, unique=True)
    password_hash = models.CharField(max_length=255)
    full_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=150, null=True)
    department = models.CharField(max_length=100, null=True)
    role = models.CharField(max_length=50, default='USER')
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'SYS_USERS'