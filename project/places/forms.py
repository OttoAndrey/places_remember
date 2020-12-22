from django import forms


class PlaceForm(forms.Form):
    title = forms.CharField(label='Название', max_length=50)
    text = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'rows': 3, "cols": 30}))
    lat = forms.DecimalField(
        max_digits=17,
        decimal_places=15,
    )
    lng = forms.DecimalField(
        max_digits=17,
        decimal_places=15,
    )
