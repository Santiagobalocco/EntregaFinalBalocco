from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import (
    TemplateView, ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Page
from .forms import PageForm



class HomeView(TemplateView):
    template_name = 'home.html'



@require_http_methods(["GET"])
def about(request):
    return render(request, 'about.html')

from django.views.generic import ListView

class PageListView(ListView):
    model = Page
    template_name = 'pages/page_list.html'    
    context_object_name = 'pages'

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
        
            qs = qs.filter(title__icontains=q)
        return qs


class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page'


class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('page_list')

    def form_valid(self, form):
        # Asignamos autor automáticamente
        form.instance.author = self.request.user
        return super().form_valid(form)



class PageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('page_list')

    def test_func(self):
        page = self.get_object()
        return page.author == self.request.user


class PageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('page_list')

    def test_func(self):
        page = self.get_object()
        return page.author == self.request.user
