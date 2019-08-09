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
    comment = Comment.objects.filter(post=post_detail).order_by('likes')
    
    return render(request, 'show/detail.html',{'post':post_detail, 'form':form, 'comment':comment, 'exhibition':exhibition})

def exhibition(request):
    posts = Post.objects
    e = get_object_or_404(Category, pk = 1)
    print(e)
    musical = Post.objects.filter(category=e)
    print(musical)
    
    return render(request, 'show/exhibition.html', {'posts' : posts, 'musical':musical})

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

def post_like(request, comment_id ) :
    # 코멘트 정보 받아옴
    post_detail=get_object_or_404(Post, pk = post_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    post = comment.post
    # post = get_object_or_404(Post, pk=post_id)
    # 사용자가 로그인 된건지 확인
    if not request.user.is_active:
        return redirect('detail', post_id=post.id)    

    #사용자 정보 받아옴
    user = User.objects.get(username=request.user)
    comment.likes.add(user)
    # print(comment.likes.filter(id=user.id).exists())
    # print(comment.likes.count())
    
    count = comment.likes.count()
    comment = Comment.objects.filter(post=post_detail).order_by('likes')

    # print(Comment.objects.filter(like=request.user.id).exists())
    # if comment.likes == user: # 이 댓글에 지금 로그인한 사용자가 좋아요 누른 적 있으면
    #     print(aa)

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