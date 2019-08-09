from django.shortcuts import render,get_object_or_404, redirect
from .models import Musical,Exhibition,Concert,Classic, Category, Post, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    posts = Post.objects
    return render(request, 'show/home.html', {'posts' : posts})

def detail(request, post_id):
    post_detail=get_object_or_404(Post, pk = post_id)
    form = CommentForm()
    comments = Comment.objects.filter(post=post_detail)
    commentss = Comment.objects.filter(post=post_detail)
    comments = sorted(comments, key=lambda c: c.likes.count(), reverse=True)

    
    return render(request, 'show/detail.html',{'post':post_detail, 'form':form, 'comments': comments, "commentss":commentss, 'exhibition':exhibition})

def exhibition(request):
    posts = Post.objects
    # category = request.GET.get('category')
    # if category == 'exhibition':
    #     exhibitions = Post.objects.filter(category=exhibition)
    # elif category == 'musical':

    # exhibition = get_object_or_404(Category, pk= 2)
    # print(exhibition)
    # exhibitions = Post.objects.filter(category=exhibition)
    # print(exhibitions)
    exhibitions = Post.objects.filter(category=2)
    return render(request, 'show/exhibition.html', {'exhibitions':exhibitions})

def musical(request):
    posts = Post.objects
    musicals = Post.objects.filter(category=1)
    return render(request, 'show/musical.html', {'musicals' : musicals })

def concert(request):
    posts = Post.objects
    concerts = Post.objects.filter(category=3)
    return render(request, 'show/concert.html', {'concerts' : concerts})

def classic(request):
    posts= Post.objects
    classics = Post.objects.filter(category=4)
    return render(request, 'show/classic.html', {'classics' : classics})

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

def post_like(request, comment_id ) :
    # 코멘트 정보 받아옴
    comment = get_object_or_404(Comment, pk=comment_id)
    post = comment.post
    print(post.comments.all)
    
    if not request.user.is_active:
        return redirect('detail', post_id=post.id)    

    #사용자 정보 받아옴
    user = User.objects.get(username=request.user)
    comment.likes.add(user)
    # print(comment.likes.filter(id=user.id).exists())
    # print(comment.likes.count())
    
    count = comment.likes.count()

    # print(Comment.objects.filter(like=request.user.id).exists())
    if comment.likes == user: # 이 댓글에 지금 로그인한 사용자가 좋아요 누른 적 있으면
        print(aa)

    #좋아요에 사용자가 존재하면
    # if comment.likes.filter(id = request.user.id).exists():
        # 사용자를 지움
        # comment.likes.remove(user)
    # else:
    #     # 아니면 사용자를 추가
    #     comment.likes.add(user)
    #포스트로 리디렉션
    return redirect('detail', post_id=post.id)
     #우리는 코멘트를 가져와서 거기다가 좋아요 기능을 만들건데
    # 코멘트마다 뭐를 하나씩 클릭하면
    # 코멘트 밑에 있는 숫자가 올라가겠끔만 하면 됨!!!
