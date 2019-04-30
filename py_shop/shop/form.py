from django import forms
from django.utils import timezone


class OrderForm(forms.Form):
    name = forms.CharField(required=True)
    last_name = forms.CharField(required=False)
    phone = forms.CharField(max_length=13, required=True)
    buying_type = forms.ChoiceField(widget=forms.Select(), choices=([("delivery", "Доставка"), ("self", "Самовывоз")]))
    sail = forms.ChoiceField(widget=forms.Select(), choices=([("cash", "Наличными"), ("cart", "Карточкой")]))
    date_delivery_true = forms.CharField(max_length=10, required=False)
    date_delivery_false = forms.CharField(max_length=0, required=False)
    day_half = forms.ChoiceField(widget=forms.Select(),
                                 choices=([("morning", "Первая"), ("evening", "Вторая")]),
                                 required=False)
    address_false = forms.CharField(max_length=0, required=False)
    address_true = forms.CharField(required=True)
    comments = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Имя"
        self.fields['last_name'].label = "Фамилия"
        self.fields['phone'].label = "Телефон"
        self.fields['sail'].label = "Способ оплаты"
        self.fields['buying_type'].label = "Способ получения"
        self.fields['address_false'].label = 'Адрес доставки'
        self.fields['address_false'].help_text = 'В случае самовывоза не заполняется'
        self.fields['address_true'].label = 'Адрес доставки'
        self.fields['address_true'].help_text = 'Обязательно укажите город'
        self.fields['comments'].label = 'Комментарии к заказу'
        self.fields['comments'].help_text = 'Оставьте свои комментарии к заказу'
        self.fields['date_delivery_true'].label = 'Желаемая дата доставки'
        self.fields['date_delivery_true'].help_text = 'В формате: "day.month.age."'
        self.fields['date_delivery_false'].label = 'Желаемая дата доставки'
        self.fields['date_delivery_false'].help_text = 'В случае самовывоза не заполняется'
        self.fields['day_half'].label = 'Укажите в какой половине дня будет доставка'
        self.fields['day_half'].help_text = 'Условия и сроки доставки смотрите в разделе "Сервис -> Доставка"'

