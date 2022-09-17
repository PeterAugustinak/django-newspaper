from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Article


TEMP_PATH = 'articles/'

class ArticleListView(ListView):
    model = Article
    template_name = f"{TEMP_PATH}/article_list.html"

    ordering = ['-date']


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = f"{TEMP_PATH}/article_create.html"
    fields = (
        "title",
        "body",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = f"{TEMP_PATH}/article_detail.html"


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = f"{TEMP_PATH}/article_update.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = f"{TEMP_PATH}/article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
