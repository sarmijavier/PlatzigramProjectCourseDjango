""" Post views """

#Django 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
#Forms
from posts.forms import PostForm, UpdatePostForm

#Models
from posts.models import Post

""" 
#utilities
from datetime import datetime

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]
 """

class PostsFeedView(LoginRequiredMixin, ListView):
    """ Return all published posts. """

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-create')
    paginate_by = 30
    context_object_name = 'posts'


class CreatePostView(LoginRequiredMixin, CreateView):
    """ Create a new post view """

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')


    def get_context_data(self, **kwargs):
        """ Add user and profile to context. """
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile


        return context
    

@login_required
def list_posts(request):
    """ List existing posts. """
    posts = Post.objects.all().order_by('-create')
    return render(request, 'posts/feed.html', {'posts': posts})


def editPost(request, username, id):
    # print(username, id)
    post = Post.objects.get(id=id)
    profile = request.user.profile

    if request.method == 'POST':
        form = UpdatePostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post.title = data['title']
            post.save()

            url = reverse('users:detail', kwargs={'username':request.user.username})
            return redirect(url)
    else: 
        form = UpdatePostForm()
    

    return render(
        request=request,
        template_name='posts/editPost.html',
        context={
            'profile': profile,
            'user': request.user,
            'post': id,
            'form':form
        }
    )