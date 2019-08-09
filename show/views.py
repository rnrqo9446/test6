from django.shortcuts import render,get_object_or_404, redirect
from .models import Musical,Exhibition,Concert,Classic, Category, Post, Comment
from .forms import CommentForm

def home(request):
    posts = Post.objects
    return render(request, 'show/home.html', {'posts' : posts})

def detail(request, post_id):
    post_detail=get_object_or_404(Post, pk = post_id)
    form = CommentForm()
    return render(request, 'show/detail.html',{'post':post_detail, 'form':form,})

def exhibition(request):
    posts = Post.objects
    return render(request, 'show/exhibition.html', {'posts' : posts})

def musical(request):
    posts = Post.objects
    return render(request, 'show/musical.html', {'posts' : posts})

def concert(request):
    posts = Post.objects
    return render(request, 'show/concert.html', {'posts' : posts})

def classic(request):
    posts = Post.objects
    return render(request, 'show/classic.html', {'posts' : posts})

def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    return redirect('detail', post_id=post.pk)

def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post = comment.post
    comment.delete()
    return redirect('detail', post_id=post.id)


# def home(request):
#     musicals=Musical.objects
#     return render(request, 'show/home.html',{'musicals':musicals})

# def musical_home(request):
#     musicals=Musical.objects
#     return render(request, 'show/musical_home.html',{'musicals':musicals})

# def musical_detail(request,musical_id):
#     musical_detail=get_object_or_404(Musical,pk= musical_id)
#     return render(request, 'show/musical_detail.html',{'musical':musical_detail})

# def exhibition_home(request):
#     exhibitions=Exhibition.objects
#     return render(request, 'show/exhibition_home.html',{'exhibitions':exhibitions})

# def exhibition_detail(request,exhibition_id):
#     exhibition_detail=get_object_or_404(Exhibition,pk= exhibition_id)
#     return render(request, 'show/exhibition_detail.html',{'exhibition':exhibition_detail})

# def concert_home(request):
#     concerts=Concert.objects
#     return render(request, 'show/concert_home.html',{'concerts':concerts})

# def concert_detail(request,concert_id):
#     concert_detail=get_object_or_404(Concert,pk= concert_id)
#     return render(request, 'show/concert_detail.html',{'concert':concert_detail})

# def classic_home(request):
#     classics=Classic.objects
#     return render(request, 'show/classic_home.html',{'classics':classics})

# def classic_detail(request,classic_id):
#     classic_detail=get_object_or_404(Classic,pk= classic_id)
#     return render(request, 'show/classic_detail.html',{'classic':classic_detail})