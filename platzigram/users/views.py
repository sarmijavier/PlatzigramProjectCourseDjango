""" User views. """

#Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import  login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.db.utils import IntegrityError

#Model
from django.contrib.auth.models import User
from posts.models import Post
#from users.models import Profile

#forms
from users.forms import ProfileForm, SignupForm




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
        return context 
    


    

@login_required
def update_profile(request):
    """ Update a user profile """

    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()
            #print(form.cleaned_data)

            url = reverse('users:detail', kwargs={'username':request.user.username})
            return redirect(url)
    else:
        form = ProfileForm()

    profile = request.user.profile

    return render(request=request, 
                    template_name='users/update_profile.html',
                    context={
                        'profile': profile,
                        'user': request.user,
                        'form':form
                    })


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


def signup(request):
    """ Signup view """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('users:login')
    else:
        form = SignupForm()
    
    return render(
        request=request,
        template_name='users/signup.html',
        context={'form':form}
    )



