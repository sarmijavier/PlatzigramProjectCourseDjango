""" Post admin classes """

#Django
from django.contrib import admin


#Models
from django.contrib.auth.models import User
from posts.models import Post 


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    """ Posts admin """

    list_display = ('pk', 'user', 'title', 'profile', 'photo')
    list_display_links = ('user', 'profile')
    list_editable = ('title', 'photo')
    search_fields = ('post__user','post__title')
    list_filter = ('create', 'modified')

    fieldsets = (
        ('Post', {
            'fields': (('user', 'photo'),),
        }),
        ('Image', {
            'fields':('image_tag',)
        }),
        ('Metadata', {
            'fields': (
                ('create', 'modified'),),
        }),
    )

    readonly_fields = ('create', 'modified', 'image_tag')

