from django import forms
from .models import BlogPost

class BlogPostForm(forms.Form):
    slug = forms.SlugField()
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    about = forms.CharField()
    time = forms.TimeField()
    date = forms.DateField(widget=forms.SelectDateWidget)
    select = forms.CharField(max_length=256, widget=forms.Select(choices=[('Model Feed', 'Model Feed'),('News Feed', 'News Feed'),('Other Feed','Other Feed')]))

class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['slug','title','content','about','time','date','select']

    def clean_slug(self, *args, **kwargs):
        slug = self.cleaned_data.get('slug')
        if len(slug) < 4:
            raise forms.ValidationError("Length of slug must be atleast 4 character")
        return slug
    
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title=title)
        if qs.exists():
            raise forms.ValidationError("Title is already exists in the database")
        return title
    
    