""" Post views """

#Django 
from django.http import HttpResponse

#utilities
from datetime import datetime

posts = [
    {
        'name': 'Mont Blac',
        'user': 'Yesica Cortés',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://i.picsum.photos/id/237/200/300.jpg?hmac=TmmQSbShHz9CdQm0NkEjx1Dyh_Y984R9LpNrpvH2D_U'
    },
    {
        'name': 'Via Láctea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Thespianartist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076',
    }
]


def list_posts(request):
    """ List existing posts. """
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user}- <i>{timestamp}</i></small></p>
            <figure>
                <img src="{picture}"/>
            </figure>
        """.format(**post))

    return HttpResponse('<br>'.join(content))
