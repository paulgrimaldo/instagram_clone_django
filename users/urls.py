from django.urls import path

from users import views
from users.views import UserDetailView

urlpatterns = [
    path(route='login/', view=views.LoginView.as_view(), name='login'),

    path(route='logout/', view=views.LogoutView.as_view(), name='logout'),

    path(route='signup/', view=views.SignUpView.as_view(), name='signup'),

    path(route='me/profile/', view=views.UpdateProfileView.as_view(), name='update'),

    path(route='<str:username>/', view=UserDetailView.as_view(), name='detail')
]
