from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('review/', views.review, name='review'),
    path('book_reservation/', views.book_reservation, name='book_reservation'),
    path('auth/', include('django.contrib.auth.urls')),  # Use built-in authentication views
]

# TODO check out this and see if needed
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)