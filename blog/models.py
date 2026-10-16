from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models


class Tag(models.Model):
    """
    Represents a tag associated with blog posts.
    """

    caption = models.CharField(max_length=20, validators=[MinLengthValidator(2)])

    def __str__(self) -> str:
        return self.caption


class Post(models.Model):
    """
    Represents a blog post.
    """

    title = models.CharField(max_length=200, validators=[MinLengthValidator(2)])
    excerpt = models.CharField(max_length=200, validators=[MinLengthValidator(10)])
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    tags = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    """
    Represents a comment on a blog post.
    """

    user_name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    date = models.DateTimeField(auto_now_add=True)
