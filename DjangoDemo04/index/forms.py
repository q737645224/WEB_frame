from django import forms
from .models import *

# 为topic控件初始化数据
TOPIC_CHOICE = (
  ('1','好评'),
  ('2','中评'),
  ('3','差评'),
)

#表示评论内容的表单控件们
#控件1 - 评论标题　- 文本框
#控件2 - Email - Email框
#控件3 - 评论内容 - Textarea
#控件4 - 评论级别　- Select
#控件5 - 是否保存　- Checkbox
class RemarkForm(forms.Form):
  # subject - input type='text'
  # label 表示的是控件前的文本
  subject=forms.CharField(label='标题')
  # email - input type='email'
  email = forms.EmailField(label='邮箱')
  # message - Textarea
  # widget=forms.Textarea,表示将当前属性变为多行文本域
  message = forms.CharField(label='内容',widget=forms.Textarea)
  # topic - Select
  topic = forms.ChoiceField(label='级别',choices=TOPIC_CHOICE)
  # isSaved - checkbox
  isSaved = forms.BooleanField(label='是否保存')

class RegisterForm(forms.ModelForm):
  #通过内部类Meta表示关联的信息
  class Meta:
    #1.指定关联的Model
    model = User
    #2.指定要生成控件的字段们
    fields = "__all__"
    #3.指定每个控件对应的label
    labels = {
      'uphone':'电话号码',
      'upwd':'登录密码',
      'uname':'用户名称',
      'uemail':'电子邮件',
    }

class LoginForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['uphone','upwd']
    labels = {
      'uphone':'注册电话',
      'upwd':'登录密码',
    }
    #指定小部件
    widgets = {
      'upwd':forms.PasswordInput(attrs={
        'placeholder':'请输入您的密码'
      })
    }

class WidgetLoginForm(forms.Form):
  uphone = forms.CharField(label='电话号码')
  #为pwd指定小部件，显示为　密码框
  # upwd = forms.CharField(label='登录密码',widget=forms.PasswordInput)
  upwd = forms.CharField(
    label='登录密码',
    widget=forms.PasswordInput(
      attrs = {
        'placeholder':'请输入密码',
        'class':'form-control',
      }
    )
  )







