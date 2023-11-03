from django.urls import path
from . import views

app_name = 'fivecart'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.detail, name='detail'),
    path('report/<int:report_id>/', views.report_detail, name='report_detail'),
    path('execute_keyfunc/', views.execute_keyfunc, name='execute_keyfunc'),  # URL 패턴 추가
    path('update_keys/', views.update_keys, name='update_keys'),
]
