from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile


class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True,
                                verbose_name=_('user'), related_name='my_profile')
    favourite_book = models.CharField(_('favourite book'),max_length=5)
