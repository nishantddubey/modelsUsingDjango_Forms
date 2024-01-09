from django import forms
from app.models import *

# Normal validation 

def validate_for_j(data):
    if data.lower().startswith('j'):
        raise forms.ValidationError("Statrts with j")

def validate_for_email(data):
    if '@' not in data:
        raise forms.ValidationError("Email Not valid")
        

# creation of input boxes

class TopicForm(forms.Form):
    topic_name = forms.CharField(validators=[validate_for_j])


class WebpageForm(forms.Form):
    tl = [[to.topic_name,to.topic_name] for to in Topic.objects.all()]
    topic_name = forms.ChoiceField(choices=tl)
    name = forms.CharField()
    url = forms.URLField()
    email = forms.EmailField(validators=[validate_for_email])
    

class AccessrecordForm(forms.Form):
    wl = [[wo.pk,wo.name] for wo in Webpage.objects.all()]
    name = forms.ChoiceField(choices=wl)
    date = forms.DateField()
    author = forms.CharField()
    
    # form class objects method validation
    def clean(self):
        name = self.cleaned_data['name']
        author = self.cleaned_data['author']
        # if name==author:
        #     raise forms.ValidationError("Name and Author Cannot be Same")

        
        if len(author)>10:
            raise forms.ValidationError("Name too Long")