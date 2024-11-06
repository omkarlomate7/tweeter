from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Tweet
from .serializers import TweetSerializer, UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TweetForm


from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to home after successful login
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')

@login_required
def home(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('home')
    else:
        form = TweetForm()
    
    tweets = Tweet.objects.all().order_by('-created_at')  # Display tweets in descending order
    return render(request, 'home.html', {'form': form, 'tweets': tweets})
# User Registration View
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Tweet Views
class TweetListCreateView(generics.ListCreateAPIView):
    queryset = Tweet.objects.all().order_by('-created_at')
    serializer_class = TweetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserTweetsView(generics.ListAPIView):
    serializer_class = TweetSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        username = self.kwargs['username']
        return Tweet.objects.filter(user__username=username)
