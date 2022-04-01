# Create your views here.
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from .forms import DonorCreationForm
from django.http import JsonResponse
from .models import Donor, Branch


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password, email=email)

                user.save()
                print("User Created")
                return redirect('/login')

        else:

            messages.info(request, "Password not matching")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def donor_create_view(request):
    form = DonorCreationForm()
    if request.method == 'POST':
        form = DonorCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donor_add')
    return render(request, 'donation.html', {'form': form})


def donor_update_view(request, pk):
    donor = get_object_or_404(Donor, pk=pk)
    form = DonorCreationForm(instance=donor)
    if request.method == 'POST':
        form = DonorCreationForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            return redirect('donor_change', pk=pk)
    return render(request, 'donation.html', {'form': form})


# AJAX
def load_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'add.html', {'branches': branches})
#     # return JsonResponse(list(branches.values('id', 'name')), safe=False)

# def donation(request):
#     return render(request,'donation.html')
