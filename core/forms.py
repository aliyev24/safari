from django import forms


class TourForm(forms.Form):
    night_from =forms.DateField(
        label='Select a date',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'})
    )
    night_till = forms.DateField(
        label='Select a date',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'})
    )
    adult = forms.IntegerField()
    child = forms.IntegerField()
