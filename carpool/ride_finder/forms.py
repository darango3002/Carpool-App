from django import forms
from .widgets import XDSoftDateTimePickerInput
from .models import Car, Ride
from address.forms import AddressField

class RideForm(forms.ModelForm):
    date_departure = forms.DateTimeField(
        label="Departure Date and Time (D/M/Y H:M)",
        input_formats=['%d/%m/%Y %H:%M'], 
        widget=XDSoftDateTimePickerInput()
    )
    
    def __init__(self, *args, **kwargs):
        self.user= kwargs.pop('user')
        super(RideForm,self).__init__(*args,**kwargs)
        self.fields['car'] = forms.ModelChoiceField(queryset=Car.objects.all().filter(user=self.user))

    class Meta:
        model = Ride
        fields = ['car', 'start', 'destination', 'date_departure', 'seats']


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ['name', 'make', 'model', 'color', 'year']