from django.urls import path
from . import views

app_name = 'myblog'
urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', views.PostListViews.as_view(), name='post_list'),
    # path('<int:id>/', views.post_detail, name='post_detail'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
]
