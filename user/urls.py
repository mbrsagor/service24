from django.urls import pathfrom django.contrib.auth import views as auth_viewsfrom .views import ProfileListViewurlpatterns = [    path('profile/', ProfileListView.as_view(), name='profile'),    path('password_change', auth_views.PasswordChangeForm, name='password_change'),]