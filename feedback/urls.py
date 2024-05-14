from django.urls import path
from . import views

# Эта строчка обязательна. 
# Без нее чуда не произойдет и namespace работать не будет
app_name = 'feedback'

urlpatterns = [
    # Главная страница
    path('', views.index, name='feedback_list'),
]