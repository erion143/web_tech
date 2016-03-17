from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=127)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title:
            raise forms.ValidationError(
                'Title can\'t be empty')
        else:
            return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if not text:
            raise forms.ValidationError(
                'Question body can\'t be empty')
        else:
            return text

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def save(self):
        if self.is_valid(): pass
        answer = Answer(text=self.cleaned_data['text'],
                        question_id=self.cleaned_data['question'])
        answer.save()
        return answer

    def clean_text(self):
        text = self.cleaned_data['text']
        if not text:
            raise forms.ValidationError(
                'Answer can\'t be empty')
        else:
            return text
