import Enum

from django.db import models


TYPE = (
    ('govt', 'GOVT'),
    ('private', 'PRIVATE'),
)

GENDER = (
    ('male', 'MALE'),
    ('female', 'FEMALE'),
    ('both', 'BOTH')
)


class OpportunityType(Enum):
    """
    Opportunity type to maintain its usage across the project
    """
    GOVT = 'govt'
    PRIVATE = 'private'


class Opportunity(models.Model):
    name = models.TextField(max_length=100)
    type = models.CharField(max_length=7, choices=TYPE, default='govt')
    brief_info = models.TextField(max_length=1000)
    age_criteria = models.IntegerField()
    gender_criteria = models.CharField(max_length=6, choices=GENDER, default='both')

    def __str__(self):
        return self.name
