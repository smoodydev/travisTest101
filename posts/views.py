# We're going to need a few more libraries apart from the standard render library, i.e get_object_404 etc

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm

# Create your views here.

def get_posts(request):
  """
  Create a view that will return a list of Posts that were published prior to 'now' and render them to the 'blogposts.html' template
  """
  # create out posts object here
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
  # use the render library to return our blogposts.html temlplate, which is going to contain out list of posts
  return render(request, 'blogposts.html', {'posts':posts})

# (post_detail) view this is going to return a single post and all the information about it
def post_detail(request, pk):
  """
  Create a view that returns a single Post object based on the post ID (pk) and render it to the 'postdetail.html' template. Or return a 404 error if the post is not found
  """
  # Right, so let's have a look at our post detail view now. So again, we want to do a get_object_or_404. It's going to get our post item based on our post ID.
  post = get_object_or_404(Post, pk=pk)
  post.views += 1
  post.save()
  return render(request, 'postdetail.html', {'post':post})

def create_or_edit_post(request, pk=None):
  """
  Create a view that allows us to create or edit a post depending if the post ID is null or not
  """

  post = get_object_or_404(Post, pk=pk) if pk else None
  # if this is a result of posting the form then we want to render out blogpost form
  if request.method == 'POST':
    form = BlogPostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
      post = form.save()
      return redirect(post_detail, post.pk)
  else:
    form = BlogPostForm(instance=post)
  return render(request, 'blogpostform.html', {'form': form})





