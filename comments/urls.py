from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.Comments, name="comments"),
    path('register/', views.Register_page, name="register"),
    path('login/', views.Login_page, name="login"),
    path('logout/', views.Logout_user, name="logout"),
    path('borrar-comentario/<int:id>', views.delete_comment, name="borrar")
]