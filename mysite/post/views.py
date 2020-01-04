from django.shortcuts import render,get_object_or_404
from django.views import generic
from.models import Post,Comment,Book,Usign
from.forms import CommentForm 
from django.http import HttpResponseRedirect




class PostList(generic.ListView):
    queryset  =  Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by  = 1
    



def post_detail(request,slug):
    template_name  = "post_detail.html"
    post = get_object_or_404(Post,slug = slug)
    comments = post.comments.filter(active =True)
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    else:
        comment_form = CommentForm()
    return render(request,template_name,{
        "post":post,
        "comments":comments,
        "new_comment":new_comment,
        "comment_form":comment_form

    })


def upload_file(request):
    books = Book.objects.all()        
    context = {
        "books":books,        
    }
    return render(request,"learn.html",context)




def display(request):
    admins = Usign.objects.all()
    context = {
        "admins":admins,
    }
    
    return render(request,"display.html",context)