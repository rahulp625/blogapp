from django.http import request
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q

# Create your views here.
from django.views import generic
from .models import Post



class PostList(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'dashboard.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        super_context = super().get_context_data(*args, object_list=object_list, **kwargs)
        super_context.update({'posts':super_context.get('object_list')})
        return super_context

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_authenticated:
            queryset = queryset.filter(published=True)
        else:
            queryset = queryset.exclude(~Q(published=True) & ~Q(author=self.request.user))
        return queryset


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blogpost_detail.html'


# class UpdatePostView(PermissionRequiredMixin,LoginRequiredMixin,generic.UpdateView):
class UpdatePostView(LoginRequiredMixin,generic.UpdateView):
    model = Post
    template_name = 'edit_blog_post.html'
    fields = ['title', 'slug', 'content', 'published','category']


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Security: A user cannot edit another user's blog from url # Throwing error because of form.instance.author
        if request.user == self.object.author or request.user.is_superuser:
            return super().get(request, *args, **kwargs)
        else:
            raise PermissionError('Only creator of the thi post can edit it.')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Security: A user cannot edit another user's blog from url # Throwing error because of form.instance.author
        if request.user == self.object.author or request.user.is_superuser:
            return super().post(request, *args, **kwargs)
        else:
            raise PermissionError('Only creator of the thi post can edit it.')        

    '''
    ipdb> self.request.resolver_match.kwargs                                                                                                                     {'slug': 'happy-diwali'}                                                      
    '''
    #     return True


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ['title', 'slug', 'content', 'published', 'category']
    template_name = 'add_post.html'
    success_url = '/post/add'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)      


class DeletePostView(LoginRequiredMixin, generic.DeleteView):
    # specify the model you want to use
    model = Post
    success_url ="/"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Security: A user cannot edit another user's blog from url # Throwing error because of form.instance.author
        if request.user == self.object.author or request.user.is_superuser:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)    
        else:
            raise PermissionError('Only creator of the thi post can edit it.')        

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user == self.object.author or request.user.is_superuser:
            return super().delete(request, *args, **kwargs)
        else:
            raise PermissionError('Only creator of the thi post can edit it.')



# @login_required(login_url = '/login')
# def add_blogs(request):
#     if request.method=="POST":
#         form = BlogPostForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             blogpost = form.save(commit=False)
#             blogpost.author = request.user
#             blogpost.save()
#             obj = form.instance
#             alert = True
#             return render(request, "add_blogs.html",{'obj':obj, 'alert':alert})
#     else:
#         form=BlogPostForm()
#     return render(request, "add_blogs.html", {'form':form})


def confirm_post_delete(request, slug): # Not required for now
    post = Post.objects.filter(slug=slug).first()
    if post:
        # if request.method == "POST":
        #     post.delete()
        #     return redirect('/')
        return render(request, 'delete_post.html', {'post':post})
    else:
        return redirect('/')


def login_view(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
        return render(request, 'login.html', {'message': "Invalid Credentials. Please try again."})
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/login')        
