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

Occupation = (
    ('agriculture', 'AGRI'),
    ('daily wage', 'DAILY WAGE'),
    ('salaried in private', 'SALARIED PRIVATE'),
    ('unemployed', 'UNEMPLOYED')

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
    annual_income_range = models.IntegerField
    source_of_livelihood = models.CharField(choices= Occupation, default = 'UNEMPLOYED')

    def __str__(self):
        return self.name
