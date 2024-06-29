from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('review/', views.review, name='review'),
    path('book_reservation/', views.book_reservation, name='book_reservation'),
]

# TODO check out this and see if needed
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)