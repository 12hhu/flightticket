from django.urls import path
from flight import views
urlpatterns = [
    path('',views.homepage),
    path('login/',views.ulogin),
    path('booking/',views.booking),
    path('booking1/',views.booking1),
    path('booking2/',views.booking2),
    path('booktickets/',views.booktickets),
    path('register/',views.register)
    
]