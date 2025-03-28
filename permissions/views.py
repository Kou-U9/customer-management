from django.shortcuts import render, get_object_or_404, redirect
from .models import ScreenPermission
from .forms import ScreenPermissionForm

def permissioin_list(request):
    permissions = ScreenPermission.objects.all()
    return render(request, 'permissions/permission_list.html', {'permissions': permissions})

def permission_edit(request, pk=None):
    if pk:
        permission = get_object_or_404(ScreenPermission,pk=pk)
    else:
        permission = None
    
    if request.method == 'POST':
        form = ScreenPermissionForm(request.POST,instance=permission)
        if form.is_valid():
            form.save()
            return redirect('permissions:permission_list')
    else:
        form = ScreenPermissionForm(instance=permission)

    return render(request, 'permissions/permission_edit.html', {'form': form})

def no_permission(request):
    return render(request, 'permissions/no_permission.html')