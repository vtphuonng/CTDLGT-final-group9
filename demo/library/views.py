from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .register_form import signup_form
from .models import books
from .register_form import AddRecordForm

def home(request):
    records = books.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Access sucessfully')
            return redirect('home')
        else:
            messages.success(request, 'login failed')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, 'logout success')
    return redirect('home')

def signup_user(request):
    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            form.save()
            # Authenticated and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password) 
            login(request, user)
            messages.success(request, "login success")
            return redirect('home')
    else:
        form = signup_form()
        return render(request, 'signup.html', {'form':form})
    return render(request, 'signup.html', {'form':form})

def book_record(request, pk):
    if request.user.is_authenticated:
        # look up record
        book_record = books.objects.get(book_id=pk)
        # for book_record in all_book_record:
        #     if book_record.book_id == f'{pk}':
        #         target_book_record = book_record
        return render(request, 'book_record.html', {'book_record':book_record})
    else:
        messages.success(request, 'U must be logged in')
        return redirect('home')
    
def delete_book(request, pk):
    if request.user.is_authenticated:
        delete_target = books.objects.get(book_id=pk)
        delete_target.delete()
        messages.success(request, 'deleted')
        return redirect('home')
    else:
        messages.success(request, 'U must be logged in')
        return redirect('home')
    
def add_book(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_book.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')

def update(request, pk):
	if request.user.is_authenticated:
		current_record = books.objects.get(book_id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
