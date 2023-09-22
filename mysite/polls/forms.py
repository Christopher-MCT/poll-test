from django import forms    
from .models import CreateQues, Choice, Question




class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class ChoiceInline(forms.Form):
    model = Choice
    extra = 3


class CreateQuestionForm(forms.ModelForm):

    class Meta:
        model = CreateQues
        fields = ('question_text',
                   'pub_date', 'choice_text', 
                   'votes',
                   'completed', )

        widgets = {
            'question_text': forms.TextInput(attrs={'class': 'form-control',}),
            'pub_date':forms.DateTimeInput( attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
            
            
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
        }

        #inlines = [ChoiceInline]
        #list_display = ('question_text', 'pub_date', 'was_published_recently')
        #list_filter = ['pub_date']
        #search_fields = ['question_text']

##django.core.exceptions.FieldError: Unknown field(s) (pub_date, votes, question_text, choice_text) specified for CreateQues
