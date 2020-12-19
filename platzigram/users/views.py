""" User views. """

#Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import  login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.db.utils import IntegrityError

#Model
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

#forms
from users.forms import SignupForm



class PostDetailView(LoginRequiredMixin, DetailView):
    
    template_name = 'users/detailpost.html'
    slug_field = 'id' 
    slug_url_kwarg = 'id' #<str:username> 
    queryset = Post.objects.all()#Concatenar peticiones, cuando busca el objeto, usa es 
    #query base para hacer más específio el query final
    context_object_name = 'post' #nombre en el template
    def get_context_data(self, **kwargs):
        """ Add user's posts to context """
        context = super().get_context_data(**kwargs)
        post= self.get_object()
        context['posts'] = Post.objects.get(id=post.id)

        return context
    



class UserDetailView(LoginRequiredMixin, DetailView):
    """ User detail view. """

    template_name = 'users/detail.html'
    slug_field = 'username' 
    slug_url_kwarg = 'username' #<str:username> 
    queryset = User.objects.all()#Concatenar peticiones, cuando busca el objeto, usa es 
    #query base para hacer más específio el query final
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """ Add user's posts to context """
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-create')
        #import pdb; pdb.set_trace()

        return context 
    


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """ Update profile View. """
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']


    def get_object(self):
        """ Return user's profile. """
        return self.request.user.profile


    def get_success_url(self):
        """ return to user's profiel. """
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


def login_view(request):
    """ Login view """

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

            
    return render(request,'users/login.html')


@login_required
def logout_view(request):
    """ Logout a user """
    logout(request)
    return redirect('users:login')


class SignupView(FormView):
    """ Users sign up view. """

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')


    def form_valid(self, form):
        """ Save form data """

        form.save()
        return super().form_valid(form)




