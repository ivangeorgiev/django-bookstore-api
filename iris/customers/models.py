from django.db import models


class AddressStatus(models.Model):
    status_id = models.BigAutoField(primary_key=True)
    address_status = models.CharField(max_length=30)

    class Meta:
        db_table = "address_status"

    def __str__(self):
        return self.address_status


class Country(models.Model):
    country_id = models.BigAutoField(primary_key=True)
    country_name = models.CharField(max_length=200)

    class Meta:
        db_table = "country"

    def __str__(self):
        return self.country_name


class Address(models.Model):
    address_id = models.BigAutoField(primary_key=True)
    street_number = models.CharField(max_length=10)
    street_name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)

    class Meta:
        db_table = "address"

    def __str__(self):
        return f"{self.street_number} {self.street_name}, {self.city}, {self.country}"


class Customer(models.Model):
    customer_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=350)
    addresses = models.ManyToManyField(Address, related_name="customers", through="CustomerAddress")

    class Meta:
        db_table = "customer"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CustomerAddress(models.Model):
    customer_address_id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)
    status = models.ForeignKey(AddressStatus, on_delete=models.RESTRICT)

    class Meta:
        db_table = "customer_address"
