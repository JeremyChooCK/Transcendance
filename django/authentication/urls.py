from django.urls import path
from authentication.views import MyTokenObtainPairView, UserCreate, oauth_callback, UserDetailView, UpdateUsernameView, ChangeProfilePictureView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', UserCreate.as_view(), name='register'),
	path('oauth/', oauth_callback, name='oauth_callback'),
    path('user_details/', UserDetailView.as_view(), name='user_details'), 
	path('edit/name', UpdateUsernameView.as_view(), name='edit_name'),
	path('edit/picture', ChangeProfilePictureView.as_view(), name='charge_profile_picture'),
]