from django.urls import path

from . import views

urlpatterns = [
    path('', views.candidates_list, name='candidates_list'),
    path('<int:pk>/', views.candidate_details, name='candidate_details'),
    path('<int:pk>/comment/', views.comment, name='comment_candidate'),
    path('add-candidate/', views.add_candidate, name='add_candidate'),
    path('<int:pk>/delete/', views.delete_candidate, name='delete_candidate'),
    path('<int:pk>/edit/', views.edit_candidate, name='edit_candidate'),
]