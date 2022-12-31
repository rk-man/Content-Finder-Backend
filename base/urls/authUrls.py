from django.urls import path

from base.views.authViews import MyTokenObtainPairView, getLoggedInUser, createUser

urlpatterns = [
    path("login/", MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("me/", getLoggedInUser, name="get-loggedin-user"),
    path("register/", createUser, name="create-user")
]
