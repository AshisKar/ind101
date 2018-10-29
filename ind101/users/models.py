from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, IntegerField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

GENDER = (
    ('male', 'MALE'),
    ('female', 'FEMALE'),
)

class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    Age = IntegerField()
    Sex = CharField(max_length=6, choices=GENDER, default='male')

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
