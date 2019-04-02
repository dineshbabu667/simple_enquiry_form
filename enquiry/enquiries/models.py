from django.db import models

from django.contrib.auth.models import User,Group

from datetime import date

from django.core.validators import RegexValidator

from django.core.urlresolvers import reverse

import os
from django.db.models import Q
from django.db.models import Count, Min, Sum, Avg



# choices

General_Choices = (
                (0,'Yes'),
                (1,'No')
    )

General_Status = (
            (0,'Active'),
            (1,'InActive'),
            (2,'Trash')
        
    )
# Create your models here.



class EnquiryForm(models.Model):
    name= models.CharField(max_length=50,verbose_name='Name')
    email = models.EmailField(max_length=50,verbose_name='Email')
    subject = models.CharField(max_length=200,verbose_name='Subject')
    message = models.TextField(verbose_name= 'Message')
    attachments = models.ImageField('Attachements',upload_to='attachments',blank=True,null=True)
    status= models.IntegerField(choices=General_Status,default=0,verbose_name='Status')
    
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now=True)
    
    
    def __str__self(self):
        return name
    
    class Meta:
        ordering = ['id']
        verbose_name = "Enquiryform"
        verbose_name_plural = "Enquiryforms"
        
