from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('review/', views.review, name='review'),
    path('book_reservation/', views.book_reservation, name='book_reservation'),
    path('login/', views.login, name='login'),
    path('logged_out/', views.logged_out, name='logged_out'),
]

# TODO check out this and see if needed
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)