from django import forms

from .models import Image


class ImageCreateForm(forms.ModelForm):
    link = forms.URLField(required=False, label='Ссылка на изображение')

    class Meta:
        model = Image
        fields = ('link', 'file')

    def clean(self):
        cleaned_data = super().clean()
        link = cleaned_data.get('link')
        file = cleaned_data.get('file')
        if not link and not file:
            raise forms.ValidationError('Загрузите файл или '
                                        'укажите ссылку на изображение!')
        if file and link:
            raise forms.ValidationError('Выберите один способ загрузки'
                                        ' изображения!')


class ImageEditForm(forms.Form):
    width = forms.IntegerField(label='Ширина', required=False, min_value=1,
                               max_value=8192)
    height = forms.IntegerField(label='Высота', required=False, min_value=1,
                                max_value=4800)

    def clean(self):
        cleaned_data = super().clean()
        width = cleaned_data.get('width')
        height = cleaned_data.get('height')
        if not width and not height:
            raise forms.ValidationError('Укажите один или оба параметра для'
                                        ' изменения изображения!')
