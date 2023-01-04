from django.urls import path
from .views import home, post, category, author, dates

urlpatterns = [
    #pagina de inicio
    path('', home, name='home'),
    
    #pagina de post
    path('post/<int:post_id>', post, name='post'),
    
    #pagina filtrado categorias
    path('category/<int:category_id>', category, name='category'),
    
    #pagina filtrado author
    path('author/<int:author_id>', author, name='author'),
    
    #pagina filtrado por fecha
    path('dates/<int:month_id>/<int:year_id>', dates, name='dates'),
    
]
