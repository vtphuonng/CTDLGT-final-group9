from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .register_form import signup_form
from .models import books
from .register_form import AddRecordForm
from .quicksort_search import *
from .quicksort_filter import *
from .sorting import *


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
        # book_record = books.objects.get(book_id=pk)
        all = books.objects.all()
        c = to_list(all)
        book_record = quick_select_by_id(c, pk)
        return render(request, 'book_record.html', {'book_record':book_record})
    else:
        messages.success(request, 'U must be logged in')
        return redirect('home')
    
def delete_book(request, pk):
    if request.user.is_authenticated:
        # delete_target = books.objects.get(book_id=pk)
        all = books.objects.all()
        c = to_list(all)
        delete_target = quick_select_by_id(c, pk)
        for i in delete_target:
            i.delete()
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

def search_by_name_records(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # look up record
            searched = request.POST['searched']
            all = books.objects.all()
            c = to_list(all)
            search_by_name_records = quick_select_by_title(c,searched)
            return render(request, 'search_by_name_records.html', {"search_by_name_records":search_by_name_records})
        else:
            return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')
    
def filter_borrowed_books(request):
    if request.user.is_authenticated:
        all = books.objects.all()
        c = to_list(all)
        filter_borrowed_books = books_filter(c, '',True)
        return render(request, 'filter_borrowed_books.html', {"filter_borrowed_books":filter_borrowed_books})
    else:
        return redirect('home')
    
def filter_unborrowed_books(request):
    if request.user.is_authenticated:
        all = books.objects.all()
        c = to_list(all)
        filter_unborrowed_books = books_filter(c, '')
        return render(request, 'filter_unborrowed_books.html', {"filter_unborrowed_books":filter_unborrowed_books})
    else:
        return redirect('home')
    
def filter_lost_books(request):
    if request.user.is_authenticated:
        all = books.objects.all()
        c = to_list(all)
        filter_lost_books = quick_select_by_id(c, 'lost')
        return render(request, 'filter_lost_books.html', {"filter_lost_books":filter_lost_books})
    else:
        return redirect('home')
    
def sorting(request):
    if request.user.is_authenticated:
        all = books.objects.all()
        c = to_list(all)
        sorting = quicksort_asc(c)
        print(sorting)
        return render(request, 'sorting.html', {"sorting":sorting})
    else:
        return redirect('home')
    
def dessorting(request):
    if request.user.is_authenticated:
        all = books.objects.all()
        c = to_list(all)
        sorting = quicksort_desc(c)
        return render(request, 'sorting.html', {"sorting":sorting})
    else:
        return redirect('home')
