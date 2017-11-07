from django import forms

from .models import Enquiry


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['full_name', 'email', 'phone', 'residence', 'property_name', 'room_type', 'arrival_date',
                  'num_of_nights', 'num_adults', 'num_children', 'num_infants']

        widgets = {
            'arrival_date': forms.TextInput(attrs={'class': 'form-control date-picker', 'placeholder': 'Arrival Date'}),
        }
