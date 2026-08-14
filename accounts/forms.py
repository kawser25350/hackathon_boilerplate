from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Account



class UserRegisterForm(UserCreationForm):
    # Custom fields will automatically append unless reordered
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    phone = forms.CharField(max_length=11)
    address = forms.CharField(max_length=150)

    class Meta:
        model = User
        # List ONLY the model fields here
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'date_of_birth',
            'phone',
            'address'
        ]
        

    def save(self, commit=True):
        user = super().save(commit=False)
        # Manually save the extra built-in fields that UserCreationForm ignores by default
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

            Account.objects.create(
                user=user,
                date_of_birth=self.cleaned_data['date_of_birth'],
                phone=self.cleaned_data['phone'],
                address=self.cleaned_data['address']
            )

        return user

class UserUpdateForm(forms.ModelForm):

    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    phone = forms.CharField(max_length=11)
    address = forms.CharField(max_length=150)

    class Meta:
        model=User
        fields=['first_name','last_name','email']


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        if self.instance.pk:
            account=self.instance.account
            self.fields['date_of_birth'].initial=account.date_of_birth
            self.fields['phone'].initial=account.phone
            self.fields['address'].initial=account.address

    def save(self,commit=True):
        user=super().save(commit=False)

        account=user.account 

        account.date_of_birth=self.cleaned_data['date_of_birth']
        account.phone=self.cleaned_data['phone']
        account.address=self.cleaned_data['address']

        if commit:
            account.save()

        return user 
