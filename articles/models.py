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
        shortened = self.body[:200]
        return shortened if len(self.body) > 200 else f'{shortened} ..'


class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        shortened = self.text[:100]
        return shortened if len(self.text) < 100 else f'{shortened} ..'

    def get_absolute_url(self):
        return reverse("article_list")
