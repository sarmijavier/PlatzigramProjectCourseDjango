""" Posts URLs. """

#Django
from django.urls import path

#Views
from posts import views


urlpatterns = [
    path(
        route='', 
        view=views.PostsFeedView.as_view(), 
        name='feed'
    ),

    path(
        route='posts/new/',
        view=views.CreatePostView.as_view(),
        name='create'
    ),

    path(
        route='<str:username>/<int:id>/',
        view=views.editPost,
        name='edit'
    )

]