from django.shortcuts import render, redirect, get_object_or_404
from .models import Visitor
from .forms import VisitorForm
from django.contrib.auth.decorators import login_required, user_passes_test

def homePage(request):
    return render(request,'home.html')

def services(request):
    return render(request, 'services.html')


def about(request):
     return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def visitor_list(request):
    visitors = Visitor.objects.all()
    return render(request, 'visitor_list.html', {'visitors': visitors})

def add_visitor(request):
    form = VisitorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('visitor_list')
    return render(request, 'visitor_form.html', {'form': form})

def update_visitor(request, id):
    visitor = get_object_or_404(Visitor, id=id)
    form = VisitorForm(request.POST or None, instance=visitor)
    if form.is_valid():
        form.save()
        return redirect('visitor_list')
    return render(request, 'visitor_form.html', {'form': form})

def delete_visitor(request, id):
    visitor = get_object_or_404(Visitor, id=id)
    visitor.delete()
    return redirect('visitor_list')


def is_staff(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff)
def staff_visitor_log(request):
    visitors = Visitor.objects.all()
    return render(request, 'visitor_list.html', {'visitors': visitors})

def staff_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('visitor_list')  
        else:
            messages.error(request, 'Invalid credentials or not a staff member.')

    return render(request, 'staff_login.html')

def visitor_action(request):
    return render(request, 'visitor_action.html')

def add_visitor(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitor_action')  
    else:
        form = VisitorForm()
    return render(request, 'visitor_form.html', {'form': form})


