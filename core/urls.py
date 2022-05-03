from django.urls import pathfrom core.views.auth import Login, Logout, SingUpViewfrom core.views.dashboard import Dashboardfrom core.views.category_view import CategoryCreateListView, CategoryUpdate, CategoryDeletefrom core.views.location_view import LocationCreateListView, LocationDeleteView, LocationFilterViewfrom core.views.homepage_view import Homepageurlpatterns = [    path('', Homepage.as_view(), name='homepage'),    path('dashboard/', Dashboard.as_view(), name='dashboard'),    # Auth    path('login/', Login.as_view(), name='login'),    path('logout/', Logout.as_view(), name='logout'),    path('signup/', SingUpView.as_view(), name='signup'),    # Categories    path('category/', CategoryCreateListView.as_view(), name='category'),    path('category/<pk>/', CategoryUpdate.as_view(), name='category_update'),    path('category/delete/<pk>/', CategoryDelete.as_view(), name='category_delete'),    # Location    path('location/', LocationCreateListView.as_view(), name='location'),    path('location/<pk>/', LocationDeleteView.as_view(), name='location_delete'),    path('location-filter/', LocationFilterView.as_view(), name='location_filter'),]