from django import forms

#声明ChoiceField要用到的数据
from index.models import Author

TOPIC_CHOICE = (
  ('1','好评'),
  ('2','中评'),
  ('3','差评'),
)

#表示评论内容的表单控件的class
#控件1-评论标题-文本框
#控件2-电子邮箱-邮件框
#控件3-评论内容-Textarea
#控件4-评论级别-下拉选择框
#控件5-是否保存-复选框
class RemarkForm(forms.Form):
  #评论标题
  # forms.CharField() - 文本框
  # label : 控件前的文本标签
  subject = forms.CharField(label='标题')
  #电子邮箱
  # forms.EmailField() - Email框
  # label : 控件前的文本标签
  email = forms.EmailField(label='邮箱')
  #品论内容
  # widget=Textarea : 将当前的单行文本框变为多行文本域
  message = forms.CharField(label='内容',widget=forms.Textarea)
  #品论级别
  # forms.ChoiceField() - 下拉列表框
  # choices : 表示当前下拉列表框中的数据,取值为元组或列表
  topic = forms.ChoiceField(label='级别',choices=TOPIC_CHOICE)
  #是否保存-复选框
  isSaved = forms.BooleanField(label='是否保存')

# class RegisterForm(forms.Form):
#   name = forms.CharField(label='姓名')
#   age = forms.IntegerField(label='年龄')
#   email = forms.EmailField(label='邮箱')

# 将Models 和 Forms 结合到一起
class RegisterForm(forms.ModelForm):
  class Meta:
    #1.指定关联的Model
    model = Author
    #2.指定生成控件的字段们
    # fields = "__all__"
    fields = ['name','age','email']
    #3.指定每个控件对应的label
    labels = {
      'name':'用户名称',
      'age':'用户年龄',
      'email':'用户邮箱',
    }

class WidgetForm1(forms.Form):
  #通过小部件的方式，为uname绑定html属性
  uname = forms.CharField(
    label='用户名称',
    widget=forms.TextInput(
      attrs = {
        'class':'form-control',
        'placeholder':'请输入用户名称'
      }
    )
  )
  #通过小部件,将upwd指定为密码框
  upwd = forms.CharField(
    label='用户密码',
    widget=forms.PasswordInput(
      attrs = {
        'class':'form-control',
        'placeholder':'请输入密码',
      }
    )
  )

class WidgetForm2(forms.ModelForm):
  class Meta:
    #指定关联的实体
    model = Author
    #指定要显示的字段
    fields = ['name','age','email']
    #指定字段对应的标签
    labels = {
      'name':'用户姓名',
      'age':'用户年龄',
      'email':'用户邮箱',
    }
    #指定字段对应的小部件
    widgets = {
      'age':forms.NumberInput(
        attrs = {
          'placeholder':'请输入年龄',
          'class':'form-control',
        }
      ),
      'email':forms.EmailInput(
        attrs = {
          'placeholder':'请输入您的电子邮箱',
          'class':'form-control',
        }
      )
    }


