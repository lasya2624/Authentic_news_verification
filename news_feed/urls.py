from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path("category/<slug:category>/", views.categorized_news, name="categorized_news"),
    path('search/', views.search_results, name='search_results'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('weather/', views.weather_report, name='weather_report'),
    path('report_misinformation/', views.report_misinformation, name='report_misinformation'),
]   
handler404 = 'news_feed.views.handler404'                               