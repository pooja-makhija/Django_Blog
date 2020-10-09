from django.conf.urls import url
from .views import (UserSignUpAPIView,
                    UserLoginAPIView,
                    GetUserListView,
                    DeleteUserView)

urlpatterns = [
    url('signup', UserSignUpAPIView.as_view()),
    url('getUserList', GetUserListView.as_view()),
    url('login', UserLoginAPIView.as_view(), name="login"),
    url('userDelete/(?P<pk>.+)', DeleteUserView.as_view(), name='user-delete')
]