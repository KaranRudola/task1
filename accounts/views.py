from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from .models import SysUser, SysModule # Naya import add kiya

# Register aur Login view (Task-1 wala) same rahega
def register(request):
    if request.method == 'POST':
        employee_number = request.POST.get('employee_number')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        SysUser.objects.create(
            employee_number=employee_number,
            full_name=full_name,
            email=email,
            password_hash=make_password(password),
            is_active=1
        )
        return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        employee_number = request.POST.get('employee_number')
        password = request.POST.get('password')

        try:
            user = SysUser.objects.get(employee_number=employee_number)
            if check_password(password, user.password_hash) and user.is_active == 1:
                user.last_login = timezone.now()
                user.save()
                request.session['user_id'] = user.user_id
                request.session['full_name'] = user.full_name
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {'error': 'Invalid credentials'})
        except SysUser.DoesNotExist:
            return render(request, 'login.html', {'error': 'User not found'})
            
    return render(request, 'login.html')

# Task-2: Dashboard Updated logic
def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('login')
    
    # Database se Master Modules fetch karna
    master_modules = SysModule.objects.filter(parent_module__isnull=True)
    
    return render(request, 'dashboard.html', {
        'name': request.session.get('full_name'),
        'master_modules': master_modules # Dynamic data pass kiya
    })