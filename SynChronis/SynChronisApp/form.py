from django.forms import ModelForm

from SynChronisApp.models import LocationTable


class LocationForm(ModelForm):
    class Meta:
        model = LocationTable
        fields = ['Location_name', 'latitude', 'longitude']