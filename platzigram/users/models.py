""" Users models """

#Django
from django.contrib.auth.models import User
from django.db import models
from django.utils.html import mark_safe

class Profile(models.Model):
    """ Profile model. 
    
    Proxy model that extends the base data with other
    information
    
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    biography =  models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def image_tag(self):
        """ Return user image """
        return mark_safe('<img src="%s" width"150" height="150" />' % (self.picture.url))
    
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        """ Return username. """
        return  self.user.username

 


