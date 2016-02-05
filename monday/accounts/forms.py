from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    is_agree = forms.BooleanField(label = '약관동의',
    error_messages = {
        'required' : '약관동의를 해주셔야 가입이 됩니다.'
    })
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'email']
    def clean_email(self):
        email = self.cleaned_data.get('email', None)
        if email:
            User = get_user_model()
            if User.objects.filter(email=email).exist():
                raise forms.ValidationError('중복된 이메일')
        return email


class SignupForm2(UserCreationForm):
    is_agree = forms.BooleanField(label = '약관동의',
        error_messages = {
            'required' : '약관동의를 해주셔야 가입이 됩니다.'
        })
    email = forms.EmailField()

    def save(self, commit=True):
        user = super(SignupForm2, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label = '3+3=?')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer', None)
        if answer != 6:
            raise forms.ValidationError('땡!!')
        return answer

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True, widget = forms.TextInput(attrs={'placeholder':'E-mail address'}))
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


#clean email filed
def clean_email(self):
    email = self.cleaned_data['email']
    try:
        User.default_manager.get(email=email)
    except User.DoesNotExist:
        return email
    raise forms.ValidationError('중복된 이메일')

def save(self, commit = True):
    user = super(RegistrationForm, self).save(commit=False)
    user.email = self.cleaned_data['email']
    if commit:
        user.is_active = False
        user.save()
    return user