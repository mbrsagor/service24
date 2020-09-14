from django.urls import pathfrom service.views.service_view import AddService, ServiceList, ServiceDetailfrom service.views.order_view import OrderList, CreateOrder, OrderDetailViewurlpatterns = [    path('add-service/', AddService.as_view(), name='add_service'),    path('service-list/', ServiceList.as_view(), name='service_list'),    path('service-detail/<pk>/', ServiceDetail.as_view(), name='service_detail'),    path('new-order/', CreateOrder.as_view(), name='create_order'),    path('order-list/', OrderList.as_view(), name='order_list'),    path('order-detail/<pk>/', OrderDetailView.as_view(), name='order_detail'),]