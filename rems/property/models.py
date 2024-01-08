from django.db import models


class Property(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title





class Unit(models.Model):
    PROPERTY_TYPES = (
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
        ('4BHK', '4BHK'),
    )

    property = models.ForeignKey(Property, related_name='units', on_delete=models.CASCADE)
    unit_type = models.CharField(max_length=10, choices=PROPERTY_TYPES)
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1)
    size = models.DecimalField(max_digits=8, decimal_places=2, help_text="Size in square feet")
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"{self.property_linked.title} - {self.unit_type}"


class Tenant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    document_proofs = models.FileField(upload_to='tenant_documents/')
    unit = models.ForeignKey(Unit, related_name='tenants', on_delete=models.CASCADE)


class RentalInformation(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    property_unit = models.ForeignKey(Property, on_delete=models.CASCADE)
    agreement_end_date = models.DateField()
    monthly_rent_date = models.IntegerField()

    class Meta:
        unique_together = ('tenant', 'property_unit')

