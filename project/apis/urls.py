from django.urls import path
from .views import WorkList, ArtistList

urlpatterns = [
    path('works/', WorkList.as_view(), name='work-list'),
    path('artists/', ArtistList.as_view(), name='artist-list'),
]
