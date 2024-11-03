# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.users import UserViewSet
from .views.channels import ChannelViewSet
from .views.requests import RequestViewSet
from .views.payments import PaymentViewSet
from django.shortcuts import render
from authemail import views

def index(request):
    # Render the welcome.html template
    return render(request, 'index.html')


router = DefaultRouter()
router.register(r'/users', UserViewSet)
router.register(r'/channels', ChannelViewSet)
router.register(r'/request', RequestViewSet)
router.register(r'/payment', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('/', index, name="index"),

    # Signup routes
    path('/signup/', views.Signup.as_view(), name='authemail-signup'),
    path('/signup/verify/', views.SignupVerify.as_view(),
         name='authemail-signup-verify'),

    # Login routes
    path('/login/', views.Login.as_view(), name='authemail-login'),
    path('/logout/', views.Logout.as_view(), name='authemail-logout'),

    # Password routes
    path('/password/reset/', views.PasswordReset.as_view(),
         name='authemail-password-reset'),
    path('/password/reset/verify/', views.PasswordResetVerify.as_view(),
         name='authemail-password-reset-verify'),
    path('/password/reset/verified/', views.PasswordResetVerified.as_view(),
         name='authemail-password-reset-verified'),

    # Email routes
    path('/email/change/', views.EmailChange.as_view(),
         name='authemail-email-change'),
    path('/email/change/verify/', views.EmailChangeVerify.as_view(),
         name='authemail-email-change-verify'),
    path('/password/change/', views.PasswordChange.as_view(),
         name='authemail-password-change'),

    # user routes
    path('/users/me/', views.UserMe.as_view(), name='authemail-me'),
]
