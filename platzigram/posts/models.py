""" Posts models. """

#Django
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe



class Post(models.Model):
    """ Post model. """
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        """ Return title and username """
        return f'{self.title} by @{self.user.username}'
    

    def image_tag(self):
        """ Return post image """
        return mark_safe('<img src="%s" width"150" height="150" />' % (self.photo.url))
    
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
