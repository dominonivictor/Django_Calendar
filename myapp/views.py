from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Entry
from .forms import EntryForm
from django.http import HttpResponseRedirect

#Render the Start page calling 'myapp/index.html'
def index(request):
    ''' Sends user to the Start Page by rendering index.html'''
    return render(request, 'myapp/index.html')

#the @login_required decorator doesn't let an anonymous user access the
#add, delete, details and calendar views, without it there would be an error
#Calendar is the sites main page, allowing the user to view his events, delete
# and add a new one
@login_required
def calendar(request):
    '''Renders only the current users Events on the Calendar/Main Page'''
    entries = Entry.objects.filter(author=request.user)
    return render(request, 'myapp/calendar.html', {'entries':entries})

#Details sends the user to the specified event
@login_required
def details(request,pk):#This is also a GET request
    entry = Entry.objects.get(id=pk)
    return render(request, 'myapp/details.html', {'entry':entry})

#Add creates a new event to the user
@login_required
def add(request):#This is a POST request
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']

            Entry.objects.create(
                name = name,
                author = request.user,
                date = date,
                description = description
            )
            return HttpResponseRedirect('/calendar')
    else:
        form = EntryForm()

    return render(request, 'myapp/form.html', {'form': form})

@login_required
def delete(request, pk):#This is a DELETE request
    '''Deletes an event on the Main Page, using the personal key(pk)'''
    if request.method == 'DELETE':
        entry = get_object_or_404(Entry, pk=pk)
        entry.delete()

    return HttpResponseRedirect('/calendar')

def signup(request):
    '''Renders a signup page, with a form for the user to signup'''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/calendar')
    else:
        form = UserCreationForm()

    return render(request, 'registration/singup.html', {'form': form})
