from django.urls import path
from .views import RegisterUserView, TweetListCreateView, UserTweetsView, login_view, logout_view, home
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tweets/', TweetListCreateView.as_view(), name='tweet_list_create'),
    path('tweets/<str:username>/', UserTweetsView.as_view(), name='user_tweets'),
    path('login/', login_view, name='login'),
    path('', home, name='home'),
    path('logout/', logout_view, name='logout'),
]
