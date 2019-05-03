from django import forms
from django.utils import timezone
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('Не верный логин')
        user = User.objects.get(username=username)
        if user and not user.check_password(password):
            raise forms.ValidationError('Неверный пароль.')


class RegistrationForm(forms.ModelForm):

    email = forms.EmailField(max_length=200, help_text='Required')
    password = forms.CharField(widget=forms.PasswordInput)
    password_check = forms.CharField(widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'password_check',
        ]

    def __init__(self, *args, **kwargs):

        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['username'].label = 'Никнейм'
        self.fields['email'].label = 'Адрес электронной почты'
        self.fields['email'].help_text = 'Пожалуйста указывайте реальный адрес'
        self.fields['password'].label = 'Пароль'
        self.fields['password'].help_text = 'Не менее 8 символов'
        self.fields['password_check'].label = 'Повторите пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        password_check = self.cleaned_data['password_check']
        email = self.cleaned_data['email']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Этот никнейм уже занят.')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким адресом уже зарегестрирвоан.')
        if password != password_check:
            raise forms.ValidationError('Пароли не совпадают.')


class OrderForm(forms.Form):

    name = forms.CharField(required=True)
    last_name = forms.CharField()
    phone = forms.CharField(max_length=13, required=True)
    buying_type = forms.ChoiceField(widget=forms.Select(), choices=([("Доставка", "Доставка"), ("Самовывоз", "Самовывоз")]))
    sail = forms.ChoiceField(widget=forms.Select(), choices=([("cash", "Наличными"), ("cart", "Карточкой")]))
    date_delivery = forms.DateField(widget=forms.SelectDateWidget(), initial=timezone.now())
    address_true = forms.CharField(required=False)
    comments = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):

        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Имя"
        self.fields['last_name'].label = "Фамилия"
        self.fields['phone'].label = "Телефон"
        self.fields['sail'].label = "Способ оплаты"
        self.fields['buying_type'].label = "Способ получения"
        self.fields['address_true'].label = 'Адрес доставки'
        self.fields['address_true'].help_text = 'Обязательно укажите город'
        self.fields['comments'].label = 'Комментарии к заказу'
        self.fields['comments'].help_text = 'Оставьте свои комментарии к заказу'
        self.fields['date_delivery'].label = 'Желаемая дата доставки'
        self.fields['date_delivery'].help_text = 'Условия и сроки доставки смотрите в разделе "Сервис -> Доставка"'

