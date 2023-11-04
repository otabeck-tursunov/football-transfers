from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('players/', hamma_futbolchilar),
    path('transfers/', transfers),
    path('clubs/', clubs),
    path('tryouts/', tryouts),
    path('about/', about),
    path('archive/', archive),
    path('mavsum/<str:son>/', mavsum_transferlari),
    path('countries/<str:nom>/', davlat_clublari),
    path('clubs/<str:nom>/', club_players),
    path('u-20-players/', u20players),
    path('stats/', stats),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
