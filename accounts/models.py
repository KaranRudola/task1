from django.db import models

# 1. User Model
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

# 2. Module Model (Ise alag rakna hai aur SysComponent se pehle)
class SysModule(models.Model):
    module_id = models.AutoField(primary_key=True)
    module_name = models.CharField(max_length=100)
    parent_module = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='submodules', 
        db_column='PARENT_MODULE_ID'
    )

    class Meta:
        db_table = 'SYS_MODULE'

# 3. Component Model
class SysComponent(models.Model):
    component_id = models.AutoField(primary_key=True)
    component_name = models.CharField(max_length=100)
    module = models.ForeignKey(
        SysModule, 
        on_delete=models.CASCADE, 
        related_name='components', 
        db_column='MODULE_ID'
    )
    url_path = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'SYS_COMPONENT'

# Task 2 Final Push