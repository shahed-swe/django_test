from django import forms

class BlogPostForm(forms.Form):
    slug = forms.SlugField()
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    about = forms.CharField()
    time = forms.TimeField()
    date = forms.DateField(widget=forms.SelectDateWidget)
    select = forms.CharField(max_length=256, widget=forms.Select(choices=[('Model Feed', 'Model Feed'),('News Feed', 'News Feed'),('Other Feed','Other Feed')]))