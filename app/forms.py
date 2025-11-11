from django import forms

g=[('male','male'),('female','female'),('other','other')]
c=[('python','python'),('django','django'),('java','java'),('sql','sql')]
class StudentDjForm(forms.Form):
    stdname=forms.CharField()
    stdage=forms.IntegerField()
    stdemail=forms.EmailField()
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #gender=forms.ChoiceField(choices=g)
    courses=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Re-enter Password',widget=forms.PasswordInput)
    #address=forms.CharField(widget=forms.Textarea)
    address=forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':20}))


