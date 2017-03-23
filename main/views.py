from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse


class Login(View):
    """Main view that login in every user before start chatting."""
    def get(self, request):
        """Return login page or the chat page if user is already logged in"""
        if request.user.is_authenticated():
            context = {
                'user': request.user.username
            }
            return render(request, 'main/chat.html', context)
        else:
            return render(request, 'main/index.html')

    def post(self, request):
        """Logs user in"""
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            context = {
                'user': username
            }
            return render(request, 'main/chat.html', context)
        else:
            return HttpResponse('wrong username or password')


class Register(View):
    """Sign up view to register users"""
    def get(self, request):
        """Return sign up form"""
        return render(request, 'main/register.html')

    def post(self, request):
        """Add user to users, login and redirect to chat page"""
        user = User.objects.create_user(request.POST['username'],
                                        request.POST['email'],
                                        request.POST['password'])
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.save()
        login(request, user)
        return HttpResponseRedirect(reverse('login'))


def log_out(request):
    """Logs an user out and redirects to index.html"""
    logout(request)
    return HttpResponseRedirect('/')


def return_404(request):
    """Handles not found pages"""
    pass
