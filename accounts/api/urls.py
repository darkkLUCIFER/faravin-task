from django.urls import path

from accounts.api.views import RegisterCreatorView, RegisterViewerView, LoginView

app_name = 'accounts'

urlpatterns = [
    path('register/creator/', RegisterCreatorView.as_view(), name='register-creator'),
    path('register/viewer/', RegisterViewerView.as_view(), name='register-viewer'),
    path('login/', LoginView.as_view(), name='login'),
]
