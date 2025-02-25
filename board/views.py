from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .models import Board
# from .forms import modelform
from django.urls import reverse_lazy, reverse

from .forms import searchform
from django.db.models import  Q
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
    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["searchform"] = searchform
        return context
    
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
    

    
class searchlist(ListView):
    model = Board
    ordering =["-pk"]
    paginate_by = 5
    search_count = 0
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context["searchform"] = searchform()
        context["keyword"] = self.request.GET.get("keyword")
        context["searchcount"] = self.search_count
        return context

    def get_queryset(self):
        keyword = self.request.GET.get("keyword")
        if keyword:
            object_list= Board.objects.filter(
                    Q(title__icontains = keyword) | 
                    Q(content__icontains =keyword)).order_by("-pk")
            self.search_count = object_list.count()
            return object_list
            
        else :
            return Board.objects.none()     

    
    