from django import forms
from .models import Board
class modelform(forms.ModelForm):
    class Meta:
        model = Board
        fields =["title","writer","content", "file"]
        
        labels ={
                "title":"제목",
                "writer":"글쓴이",
                "content":"내용",
                "file":"파일"
        }
        weights = {
            "title":forms.Textarea(attrs={"class":"form-control"}),
            "content":forms.Textarea(attrs ={"class":"form-control"})
        }
        
class searchform(forms.Form):
    keyword = forms.CharField(label ="키워드",max_length=20)