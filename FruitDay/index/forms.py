from django import forms

from index.models import Users


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['uphone','upwd']
        labels = {
            'uphone':'手机号',
            'upwd':'密码',
        }
        widgets = {
            'uphone': forms.TextInput(attrs={
                'placeholder': '请输入手机号',
                'class': 'form-control',
            }),
            'upwd': forms.PasswordInput(attrs={
                'placeholder': '请输入6-20位的字符',
                'class': 'form-control',
            })
        }

