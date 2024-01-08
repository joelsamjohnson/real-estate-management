from django.forms import ModelForm
from .models import Property, Tenant


class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'address', 'location', 'description']


class TenantAssignmentForm(ModelForm):
    class Meta:
        model = Tenant
        fields = ['name']

    def __init__(self):
        super().__init__()
        self.fields['unit'].queryset = Unit.objects.all()


        # fields = ['property_linked', 'unit_type', 'rent_cost', 'bedrooms', 'bathrooms', 'size', 'image']
