from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user_qs = User.objects.filter(username=username)
            if user_qs.count()==0:
                raise forms.ValidationError("This user does not exist") 
            else:
                user = user_qs.first()
                if not user.check_password(password):
                    raise forms.ValidationError("Incorrect Password")
        return super(UserLoginForm, self).clean()

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = fields = [
            'username',
            'email',
            'password',
        ]