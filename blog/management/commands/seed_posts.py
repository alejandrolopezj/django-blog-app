from typing import Any

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandParser
from faker import Faker

from blog.models import Comment, Post, Tag

DEMO_AUTHOR_USERNAME = "demo_author"
FAKER_LOCALE = "en_US"
FAKER_SEED = 42
DEMO_IMAGE_NAMES = (
    "posts/karacis-studio-TFQIyR8-lDI-unsplash.jpg",
    "posts/tasha-kostyuk-roPGTtmZZ5U-unsplash.jpg",
    "posts/tasha-kostyuk-aNrC8UbXlOI-unsplash.jpg",
    "posts/tasha-kostyuk-bCNkCpUXe5c-unsplash.jpg",
    "posts/public-domain-vectors-YIETA5vgvtA-unsplash.jpg",
    "posts/sasha-lend-W_a-1en5dPk-unsplash.jpg",
    "posts/public-domain-vectors-4hIiBgBG8Rs-unsplash.jpg",
    "posts/public-domain-vectors-ygxlQaDvZ-c-unsplash.jpg",
    "posts/tasha-kostyuk-iO4QApFb6E4-unsplash.jpg",
    "posts/hendi-perkasa-0Gt1cvp5OVs-unsplash.jpg",
    "posts/public-domain-vectors-0rklfdr33D4-unsplash.jpg",
    "posts/public-domain-vectors-QFls2g2-rR4-unsplash.jpg",
)

DEMO_POSTS = (
    {
        "title": "My First Project with Django",
        "slug": "my-first-project-with-django",
        "excerpt": "The first steps I took to build a blog with Django.",
        "content": "Django provides a clear structure for turning a Python idea into a web application. In this project I am learning how models, views, templates, and URLs work together to deliver a complete blog.",
        "tags": ("Django", "Python"),
    },
    {
        "title": "How to Organize a Django Application",
        "slug": "how-to-organize-a-django-application",
        "excerpt": "A practical look at keeping a Django project easy to navigate.",
        "content": "A well-organized Django application makes future changes easier to understand. I keep domain logic inside the relevant app, use descriptive names, and prefer small, focused modules over one large file.",
        "tags": ("Django", "Good practices"),
    },
    {
        "title": "Models and Relationships in Django",
        "slug": "models-and-relationships-in-django",
        "excerpt": "What I learned about representing blog data with Django models.",
        "content": "Django models describe the data that an application needs and provide a Python interface for querying it. Foreign keys and many-to-many relationships let posts connect naturally with authors, comments, and tags.",
        "tags": ("Django", "Python"),
    },
    {
        "title": "An Introduction to the Django Admin",
        "slug": "an-introduction-to-the-django-admin",
        "excerpt": "Why the built-in admin is useful while developing a content site.",
        "content": "The Django admin gives a project a useful management interface with very little setup. Customizing list displays, filters, and prepopulated fields makes everyday content management faster and more consistent.",
        "tags": ("Django", "Good practices"),
    },
    {
        "title": "Forms and Validation",
        "slug": "forms-and-validation",
        "excerpt": "How forms help keep user input safe and predictable.",
        "content": "Forms provide a boundary between user input and application data. By validating fields before saving them, the application can give useful feedback while protecting the integrity of the database.",
        "tags": ("Django", "Testing"),
    },
    {
        "title": "Template Inheritance in Django",
        "slug": "template-inheritance-in-django",
        "excerpt": "Reducing repetition with base templates and reusable includes.",
        "content": "Template inheritance allows shared layout elements to live in one base template. Reusable blocks and includes keep individual pages focused on their own content and make visual changes easier to apply consistently.",
        "tags": ("Django", "Good practices"),
    },
    {
        "title": "URLs and Class-Based Views",
        "slug": "urls-and-class-based-views",
        "excerpt": "A comparison of URL routing and reusable view behavior.",
        "content": "URL patterns connect a browser request to the code that should handle it. Class-based views are especially useful for common behaviors such as listing objects, while function-based views remain a good choice when a flow is highly specific.",
        "tags": ("Django", "Python"),
    },
    {
        "title": "Using Git in Personal Projects",
        "slug": "using-git-in-personal-projects",
        "excerpt": "Small habits that make a personal project easier to evolve.",
        "content": "Git makes experimentation safer because each meaningful change can be recorded and reviewed. Clear commits, a useful README, and a focused history also make it easier for another developer to understand the project.",
        "tags": ("Good practices", "Python"),
    },
    {
        "title": "The Value of Automated Tests",
        "slug": "the-value-of-automated-tests",
        "excerpt": "Why a small test suite can improve confidence in every change.",
        "content": "Automated tests turn expected behavior into an executable safety net. Even a few tests around models, views, and management commands can catch regressions early and make refactoring less risky.",
        "tags": ("Testing", "Good practices"),
    },
    {
        "title": "Good Practices for Python Projects",
        "slug": "good-practices-for-python-projects",
        "excerpt": "Principles I use to keep Python code readable and maintainable.",
        "content": "Readable code usually starts with simple responsibilities, descriptive names, and predictable interfaces. Formatting tools, focused functions, and meaningful documentation help a project remain approachable as it grows.",
        "tags": ("Python", "Good practices"),
    },
    {
        "title": "Building a Responsive Blog Layout",
        "slug": "building-a-responsive-blog-layout",
        "excerpt": "Lessons from adapting a blog interface to different screen sizes.",
        "content": "A responsive layout should preserve readable content instead of only shrinking desktop elements. Flexible widths, sensible breakpoints, and a mobile-first review make the blog more comfortable to use on every device.",
        "tags": ("Good practices", "Django"),
    },
    {
        "title": "The Next Improvements for This Blog",
        "slug": "the-next-improvements-for-this-blog",
        "excerpt": "Ideas for continuing to improve this Django learning project.",
        "content": "This blog is a practical record of my progress with Django and Python. Next steps include improving the content, expanding test coverage, and preparing the project for a production deployment with environment-based settings.",
        "tags": ("Django", "Testing", "Good practices"),
    },
)


def build_demo_content(readable_content: str, faker: Faker) -> str:
    """Build post content with reproducible generated paragraphs.

    :param readable_content: The manually written introductory content.
    :param faker: The seeded Faker instance used to generate filler text.
    :return: The introductory content followed by three generated paragraphs.
    """
    return f"{readable_content} {faker.paragraph(nb_sentences=10)}\n\n{faker.paragraph(nb_sentences=15)}\n\n{faker.paragraph(nb_sentences=15)}"


def build_demo_comment(faker: Faker) -> dict[str, str]:
    """Build the data for one generated demonstration comment.

    :param faker: The seeded Faker instance used to generate the comment data.
    :return: A mapping containing the comment author's name, email, and text.
    """
    sentence_count = faker.random_int(min=4, max=8)
    return {
        "user_name": faker.name(),
        "user_email": faker.email(),
        "text": " ".join(faker.sentences(nb=sentence_count)),
    }


class Command(BaseCommand):
    help = "Create or update the twelve demonstration blog posts and comments."

    def add_arguments(self, parser: CommandParser) -> None:
        """Define the command-line arguments accepted by this command.

        :param parser: The parser used to register management command options.
        """
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Delete the demonstration posts before creating them again.",
        )

    def handle(self, *args: str, **options: Any) -> None:
        """Create or update the demonstration posts and their comments.

        :param args: Positional arguments passed to the management command.
        :param options: Parsed command-line options, including ``reset``.
        """
        demo_slugs = [post_data["slug"] for post_data in DEMO_POSTS]
        faker = Faker(FAKER_LOCALE)
        faker.seed_instance(FAKER_SEED)

        if options["reset"]:
            deleted_count, _ = Post.objects.filter(slug__in=demo_slugs).delete()
            self.stdout.write(f"Deleted {deleted_count} demonstration post(s).")

        author, _ = User.objects.get_or_create(
            username=DEMO_AUTHOR_USERNAME,
            defaults={
                "first_name": "Alejandro",
                "last_name": "López",
                "email": "alejandro@example.com",
            },
        )

        tag_cache = {
            caption: Tag.objects.get_or_create(caption=caption)[0]
            for caption in {
                tag for post_data in DEMO_POSTS for tag in post_data["tags"]
            }
        }

        for index, post_data in enumerate(DEMO_POSTS):
            tags = [tag_cache[caption] for caption in post_data["tags"]]
            post, created = Post.objects.update_or_create(
                slug=post_data["slug"],
                defaults={
                    "title": post_data["title"],
                    "excerpt": post_data["excerpt"],
                    "content": build_demo_content(post_data["content"], faker),
                    "image": DEMO_IMAGE_NAMES[index],
                    "author": author,
                },
            )
            post.tags.set(tags)
            for _ in range(faker.random_int(min=1, max=3)):
                comment_data = build_demo_comment(faker)
                Comment.objects.update_or_create(
                    post=post,
                    user_email=comment_data["user_email"],
                    defaults={
                        "user_name": comment_data["user_name"],
                        "text": comment_data["text"],
                    },
                )
            action = "Created" if created else "Updated"
            self.stdout.write(f"{action}: {post.title}")

        self.stdout.write(
            self.style.SUCCESS(
                f"Ready: {len(DEMO_POSTS)} demonstration posts are available."
            )
        )
