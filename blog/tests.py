from io import StringIO

from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase

from blog.models import Comment, Post


class SeedPostsCommandTests(TestCase):
    def test_creates_twelve_posts_with_authors_and_tags(self):
        call_command("seed_posts", stdout=StringIO())

        self.assertEqual(Post.objects.count(), 12)
        self.assertEqual(User.objects.filter(username="demo_author").count(), 1)
        self.assertTrue(all(post.tags.exists() for post in Post.objects.all()))
        self.assertTrue(all(post.image.name for post in Post.objects.all()))
        self.assertEqual(
            Post.objects.values_list("image", flat=True).distinct().count(), 12
        )
        self.assertTrue(all("\n" in post.content for post in Post.objects.all()))
        self.assertTrue(
            all(1 <= post.comments.count() <= 3 for post in Post.objects.all())
        )
        self.assertTrue(
            all(4 <= comment.text.count(".") <= 8 for comment in Comment.objects.all())
        )

    def test_is_idempotent(self):
        call_command("seed_posts", stdout=StringIO())
        first_contents = dict(Post.objects.values_list("slug", "content"))
        first_comments = dict(Comment.objects.values_list("user_email", "text"))
        call_command("seed_posts", stdout=StringIO())
        second_contents = dict(Post.objects.values_list("slug", "content"))
        second_comments = dict(Comment.objects.values_list("user_email", "text"))

        self.assertEqual(Post.objects.count(), 12)
        self.assertEqual(User.objects.filter(username="demo_author").count(), 1)
        self.assertEqual(first_contents, second_contents)
        self.assertEqual(first_comments, second_comments)
        self.assertEqual(Comment.objects.count(), len(first_comments))

    def test_reset_recreates_only_demonstration_posts(self):
        Post.objects.create(
            title="Personal post",
            excerpt="This post should not be deleted.",
            content="This is content for a personal post.",
            slug="personal-post",
            image="posts/coding.jpg",
        )

        call_command("seed_posts", stdout=StringIO())
        call_command("seed_posts", "--reset", stdout=StringIO())

        self.assertEqual(Post.objects.count(), 13)
        self.assertTrue(Post.objects.filter(slug="personal-post").exists())
