"""
    Platzigram URLs module.

    path('hello-world/', local_views.hello_world, name="hello_world"),
    path('sorted/', local_views.sort_integers, name="sort"),
    path('hi/<str:name>/<int:age>', local_views.say_hi, name="hi" ),
"""

#Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path(r'', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
