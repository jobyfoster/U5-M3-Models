from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name


def create_contact(name, email, phone, is_favorite):
    contact = Contact.objects.create(
        name=name, email=email, phone=phone, is_favorite=is_favorite
    )
    return contact


def all_contacts():
    return Contact.objects.all()


def find_contact_by_name(name):
    try:
        return Contact.objects.get(name=name)
    except Contact.DoesNotExist:
        return None


def favorite_contacts():
    return Contact.objects.filter(is_favorite=True)


def update_contact_email(name, new_email):
    contact = Contact.objects.get(name=name)
    contact.email = new_email
    contact.save()


def delete_contact(name):
    Contact.objects.get(name=name).delete()
