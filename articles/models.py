from django.conf import settings
from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )

    class Meta:
        app_label = "articles"

    def __str__(self):
        short = f'{self.title[:20]} ..'
        return f'{short if len(self.title) >= 20 else self.title} ' \
               f'| by {self.author}'

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})

    @property
    def shortened_body(self):
        return f'{self.body[:200]} ...'
