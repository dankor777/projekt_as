from django.urls import path
from .views import IndexView, Postview,DodajPostView, EdytujPostView, UsunPostView, DodajKomnetarzView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>', Postview.as_view(), name='post-widok'),
    path('dodaj_post/',DodajPostView.as_view(), name='dodaj_post'),
    path('edytuj_post/<int:pk>',EdytujPostView.as_view(), name='edytuj_post'),
    path('usun_post/<int:pk>/delete',UsunPostView.as_view(), name='usun_post'),
    path('post/<int:pk>/dodaj_komentarz/',DodajKomnetarzView.as_view(), name='dodaj_komentarz'),
]
