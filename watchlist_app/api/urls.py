from django.urls import include, path
from watchlist_app.api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', StreamPlatformAV, basename='streamplatform')

urlpatterns = [
    path('show/list/', WatchListAV.as_view(), name='movie_list'),
    path('show/<int:pk>/', MovieDetailAV.as_view(), name="movie_detail"),

    path('', include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name='stream_platform_list'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream_platform_detail'),

    # #(Selected movie) reviews
    # path('review/', ReviewListAV.as_view(), name='review_list'),

    # #selected review
    # path('review/<int:pk>/', ReviewDetailAV.as_view(), name='review_detail'),
    path('<int:pk>/review', ReviewListAV.as_view(), name='review_create'),
    path('review/<int:pk>/', ReviewDetailAV.as_view(), name='review_detail'),
]

