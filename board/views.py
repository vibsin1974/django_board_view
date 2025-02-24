from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .models import Board
# from .forms import modelform
from django.urls import reverse_lazy, reverse
# Create your views here.
class create(CreateView):
    model = Board
    # form_class = modelform
    fields =["title","writer","content","file"]
    success_url = reverse_lazy("board:list")
    
    def get_form(self):
        form = super().get_form()
        form.fields["title"].label = "제목"
        form.fields["writer"].label ="글쓴이"
        form.fields["content"].label="내용"
        form.fields["file"].label="파일"
        return form
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["label"] = "쓰기"
        return context
    
class list(ListView):
    model = Board   
    ordering =["-pk"]
    
class detail(DetailView):
    model = Board
    
    def get_object(self):
        object = super().get_object()
        object.increase_read_count()
        return object
    

class edit(UpdateView):
    model = Board
    fields =["title","writer","content","file"]
    success_url = reverse_lazy("board:list")
    
    def get_form(self):
        form = super().get_form()
        form.fields["title"].label = "제목"
        form.fields["writer"].label ="글쓴이"
        form.fields["content"].label="내용"
        form.fields["file"].label="파일"
        form.fields["writer"].disabled = True
        return form
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context["label"] = "수정"
        return context
    
class delete(DeleteView):
    model = Board
    success_url = reverse_lazy("board:list")
    

    
    