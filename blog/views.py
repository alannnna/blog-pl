from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from blog.models import *


# Helper for index; prevents repetition of paging code. Also should make it
# easy to add other ways to sort the index
def get_ordered_posts(which, post_author):
    if which == "by_author":
        return BlogPost.objects.filter(author=post_author).order_by('-pub_date')
    else:  # which == "by_date"
        return BlogPost.objects.order_by('-pub_date')


# Index of blog posts. Paged and sorted by date.
def index(request, page='1', which="by_date", post_author=None):
    posts_per_page = 10
    start_id = (int(page)-1) * posts_per_page
    end_id = start_id + posts_per_page   
    ordered_posts = get_ordered_posts(which, post_author) 
    prev_page = str(int(page)-1) if int(page)-1 != 0 else None
    next_page = str(int(page)+1) if len(ordered_posts) > end_id else None

    page_of_posts = ordered_posts[start_id:end_id]

    context = { 'page_of_posts': page_of_posts,
                'prev_page': prev_page,
                'curr_page': page,
                'next_page': next_page,
                'author': post_author }
    return render(request, 'blog/index.html', context)


# Helper for calling index with which="by_author", which filters
# index results by author
def indexByAuthor(request, page='1', post_author=""):
    return index(request, page, "by_author", post_author)


# Post composition page
def writePost(request):
    return render(request, 'blog/write.html', {})


# Action of saving post
def savePost(request):
    new_post = BlogPost.objects.create(
        title=request.POST['post_title'],
        author=request.POST['post_author'],
        text=request.POST['post_meat'],
        pub_date=timezone.now())
    new_post.save()
    return HttpResponseRedirect("/post/" + str(new_post.id))


# Post display page and comment composition page
def postDetail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)  #pk?
    comments = post.comment_set.all()

    context = { 'post': post,
            'comments': comments }
    return render(request, 'blog/postdetail.html', context)


# Action of posting comment
def postComment(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    new_comment = post.comment_set.create(
        author=request.POST['comment_author'], 
        text=request.POST['comment_meat'], 
        pub_date=timezone.now())
    post.num_comments += 1
    new_comment.save()
    post.save()
    return HttpResponseRedirect("/post/" + str(post_id))


