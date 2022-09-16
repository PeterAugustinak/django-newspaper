from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Article


TEMP_PATH = 'articles/'

class ArticleListView(ListView):
    model = Article
    template_name = f"{TEMP_PATH}/article_list.html"


class ArticleCreateView(CreateView):
    model = Article
    template_name = f"{TEMP_PATH}/article_create.html"
    fields = (
        "title",
        "body",
        "author",
    )


class ArticleDetailView(DetailView):
    model = Article
    template_name = f"{TEMP_PATH}/article_detail.html"


class ArticleUpdateView(UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = f"{TEMP_PATH}/article_update.html"


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = f"{TEMP_PATH}/article_delete.html"
    success_url = reverse_lazy("article_list")

