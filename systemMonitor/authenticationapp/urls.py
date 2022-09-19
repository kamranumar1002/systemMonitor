from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login/',views.loginUser, name='login'),
    path('clients/',views.viewClients, name='clients'),
    path('sites/<str:id>/',views.viewSites, name='sites'),
    path('all-sites/',views.viewAllSites, name='all-sites'),
    path('systems/<int:id>',views.viewSystems, name='systems'),
    path('all-systems/',views.viewAllSystems, name='all-systems'),
    path('system-detail/<str:id>',views.systemDetail, name='system-detail'),
    path('logout/',views.logoutUser, name='logout'),
    path('search-systems/',views.searchSystems, name='search-systems'),
    path('search-sites/',views.searchSites, name='search-sites'),
    path('search-clients/',views.searchClients, name='search-clients'),
    path('search-dashboard/',views.searchDashboard, name='search-dashboard'),
]