from django.urls import path
from doge import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('s', views.index, name="home"),
    path('about-us', views.about, name="about"),
    path('Jack-russel-terier', views.jack, name="jack"),
    path('Siba-inu', views.Siba, name="siba"),
    path('Bull_terrier', views.bull_terrier, name="bull"),
    path('', views.bookList, name='books_url'),
    path('book/<int:id>/', views.GetBook, name='book_url'),
    path('dog/<int:id>/', views.GetDog, name='dog_url'),
    path('kit/<int:id>/', views.GetKit, name='kit_url'),
    path('delete_Book/<int:id>/', views.delete_Book),
    path('edit/<int:id>/', views.edit),
    path('create_book/', views.create_book),
    path('delete_Author/<int:idauthor>/', views.delete_Author),
    path('edit_Author/<int:idAuthor>/', views.edit_Author),
    path('create/', views.create),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=staticfiles_urlpatterns()