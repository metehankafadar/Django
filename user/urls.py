from django.urls import path

from . import views

urlpatterns = [
    # ex: /user/
    path('', views.index, name='index'),
    #path('addcomment/<int:id>', views.addComment, name='addcomment')


]