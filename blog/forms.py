from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Your Name",
            "user_email": "Your E-mail",
            "text": "Your Comment"
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty",
                "max_length": "Please enter a shorter name"
            },
            "user_email": {
                "required": "Your e-mail must not be empty",
                "max_length": "Please enter a shorter email",
                "invalid": "Please enter a valid email address"
            },
            "text": {
                "required": "You can't post an empty comment",
                "max_length": "Please enter a shorter comment",
            }
        }
