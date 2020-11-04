from django.urls import pathfrom django.contrib.auth import views as auth_viewsfrom .views import *urlpatterns = [    path('profile/', ProfileListView.as_view(), name='profile'),    path('profile-update/<pk>/', ProfileUpdateView.as_view(), name='profile_update'),    path('user-list/', UserListView.as_view(), name='user_list'),    path('user-list/<username>/', UserDeleteView.as_view(), name='delete_user'),    path('user-detail/<pk>/', UserDetailView.as_view(), name='user_detail'),    path('update-agent-profile/<pk>/', UpdateAgentProfile.as_view(), name='update_agent_profile'),    path('agent-profile/', AgentProfile.as_view(), name='agent_profile'),    path('agent-list/', ListOfAgent.as_view(), name='agent_list'),    path('delete-agent/<int:id>/', DeleteAgent.as_view(), name='delete_agent'),    path('agent-filter', AgentFilterView.as_view(), name='agent_filter'),    path('password_change', auth_views.PasswordChangeForm, name='password_change'),]