from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db.models import Q
from django.db import models, transaction
from django.db.utils import OperationalError

def get_user_file(instance, filename):
    return 'users/{0}_{1}_{2}'.format(instance.name, instance.email, filename)

class UserAbstract(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100, default='')  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=20, default='')  # Field name made lowercase.
    credit_card = models.CharField(db_column='CREDIT_CARD', max_length=25, default='')  # Field name made lowercase.
    contact = models.CharField(db_column='CONTACT', blank=True, null=True, max_length=16)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=100, default='')  # Field name made lowercase.
    image = models.ImageField(db_column='IMAGE', max_length=100, upload_to=get_user_file, null=True)
    wallet = models.IntegerField(db_column='WALLET', default=0)
    
    def __str__(self):
        return self.name

    class Meta:
        abstract = True

@python_2_unicode_compatible
class User(UserAbstract):
    def __str__(self):
        return self.name ;
    class Meta:
        managed = True
        db_table = 'User'