from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy , include
urlpatterns = [
    # ==================== HOME ====================
    path('', views.home, name='home'),
    path('accept-food/<int:id>/', views.accept_food, name='accept_food'),

    # ==================== AUTH ====================
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    


    path('logout/',LogoutView.as_view(next_page=reverse_lazy('home')),name='logout'),

    # ==================== DASHBOARD ROUTER ====================
    path('dashboard/', views.dashboard_router, name='dashboard_router'),
    path('delete-donation/<int:donation_id>/',views.delete_donation,name='delete_donation'),
    # ==================== ROLE DASHBOARDS ====================
    path('dashboard/donor/', views.dashboard_donor, name='dashboard_donor'),
    path('dashboard/ngo/', views.dashboard_ngo, name='dashboard_ngo'),
    path('dashboard/delivery/', views.dashboard_delivery, name='dashboard_delivery'),
    path('dashboard/admin/', views.dashboard_admin, name='dashboard_admin'),
    path('admin-portal/', views.admin_portal, name='admin_portal'),
    path('request-food/', views.request_food, name='request_food'),
    path('api/pickup/<int:id>/complete/', views.complete_pickup),
    path('api/pickups/', views.get_assigned_pickups, name='assigned_pickups'),
    path('add-food/', views.add_food, name='add_food'),
    # ==================== FOOD FEATURES ====================
    path('edit-donation/<int:donation_id>/', views.edit_donation, name='edit_donation'),
    path('add-donation/', views.add_food, name='add_food'),

    # 🔥 NEXT (we will build soon)
    path('accept-food/<int:id>/', views.accept_food, name='accept_food'),
    path('mark-delivered/<int:id>/', views.mark_delivered, name='mark_delivered'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)