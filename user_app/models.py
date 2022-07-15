
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
    


class Address(models.Model):
    """
    Address Model
    Defines the attributes of an Address
    """
    street = models.CharField(_("Street"), max_length=50)
    city = models.CharField(_("City"), max_length=50)
    state = models.CharField(_("state"), max_length=50)
    zip = models.IntegerField(_("Zip"))
    # user = models.OneToOneField(Parent, on_delete=models.CASCADE, related_name='address')
    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self):
        return self.city
    
class Parent(models.Model):
    """
    Parent Model
    Defines the attributes of a Parent
    """
    first_name = models.CharField(_("First Name"), max_length=50,null=False,blank=False)
    last_name = models.CharField(_("Last Name"), max_length=50,null=False,blank=False)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _("Parent")
        verbose_name_plural = _("Parents")

    def __str__(self):
        return self.first_name

class Child(models.Model):
    """
    Child Model
    Defines the attributes of a Child
    """
    first_name = models.CharField(_("First Name"), max_length=50,null=False,blank=False)
    last_name = models.CharField(_("Last Name"), max_length=50,null=False,blank=False)
    parent = models.ForeignKey(Parent, verbose_name=_("children"), on_delete=models.CASCADE, related_name='children')

    class Meta:
        verbose_name = _("Child")
        verbose_name_plural = _("Children")

    def __str__(self):
        return self.first_name

