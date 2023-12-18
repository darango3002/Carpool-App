from django import forms
from .models import Car, Ride

class RideForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user= kwargs.pop('user')
        super(RideForm,self).__init__(*args,**kwargs)
        self.fields['car'] = forms.ModelChoiceField(queryset=Car.objects.all().filter(user=self.user))


    class Meta:
        model = Ride
        fields = ['car', 'start', 'destination', 'date_departure', 'seats']


class CarForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     self.user= kwargs.pop('user')
    #     super(RideForm,self).__init__(*args,**kwargs)
    #     self.fields['car'] = forms.ModelChoiceField(queryset=Car.objects.all().filter(user=self.user))

    class Meta:
        model = Car
        fields = ['name', 'make', 'model', 'color', 'year']