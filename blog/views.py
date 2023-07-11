from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, \
    UpdateView, DeleteView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, \
    CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import GenericAPIView
from .serializers import BlogPostSerializer
from django.urls import reverse_lazy
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .models import BlogPost

# Create your views here.


class BlogListView(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = 'blog_list.html'
    context_object_name = 'blogs'


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = get_object_or_404(self.model, pk=self.kwargs.get('pk'))
        return obj


class BlogCreateView(LoginRequiredMixin, CreateView):
    permission_classes = [IsOwnerOrReadOnly]
    model = BlogPost
    template_name = 'blog_form.html'
    success_url = reverse_lazy('blog_list')
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    permission_classes = [IsOwnerOrReadOnly]
    model = BlogPost
    template_name = 'blog_form.html'
    success_url = reverse_lazy('blog_list')
    fields = ['title', 'content', 'image']


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    permission_classes = [IsOwnerOrReadOnly]
    model = BlogPost
    template_name = 'blog_confirm_delete.html'
    success_url = reverse_lazy('blog_list')
    context_object_name = 'post'


class BlogAPIView(GenericAPIView, ListModelMixin,
                  CreateModelMixin, UpdateModelMixin, RetrieveModelMixin,
                  DestroyModelMixin):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SignupPageView(View):
    def get(self, request):
        return render(request, 'registration/signup.html', {})

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            messages.error(request, "Both of the passwords don't match")
            return render(request, 'registration/signup.html', {})

        my_user = User.objects.create(username=username, email=email)
        my_user.set_password(pass1)
        my_user.save()

        return redirect('login')


class LoginPageView(View):
    def get(self, request):
        return render(request, 'registration/login.html', {})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('blog_list')
        else:
            messages.error(request, "Username or password is incorrect!")

        return render(request, 'registration/login.html', {})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
