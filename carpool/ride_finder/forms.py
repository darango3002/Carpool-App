from django import forms
from .models import User_Car, Ride

class RideForm(forms.ModelForm):
    user_car = forms.ModelChoiceField(queryset=User_Car.objects.all().filter())

    def __init__(self, *args, **kwargs):
        self.user= kwargs.pop('user')
        super(RideForm,self).__init__(*args,**kwargs)
        self.fields['user_car'] = forms.ModelChoiceField(queryset=User_Car.objects.all().filter(user=self.user))


    class Meta:
        model = Ride
        fields = ['user_car', 'start', 'destination', 'date_departure', 'seats']