# -*- coding: utf-8  -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from  django.core.urlresolvers import reverse

'''from taggit.managers import TaggableManager'''

college_choices = (
    ('M', u'كلية الطب'),
    ('A', u'كلية العلوم الطبية التطبيقية'),
    ('P', u'كلية الصيدلة'),
    ('D', u'كلية طب الأسنان'),
    ('B', u'كلية العلوم و المهن الصحية'),
    ('N', u'كلية التمريض'),
    ('I', u' كلية الصحة العامة والمعلوماتية الصحية'),
)

city_choices = (
    ('R', u'الرياض'),
    ('J', u'جدة'),
    ('A', u'الأحساء'),
)
gender_choices = (
    ('F', u'طالبات'),
    ('M', u'طلاب'),
)
university_choics = (
    ('KHS' , u'جامعة الملك سعود بن عبدالعزيز للعلوم الصحية'),
    ('KFU', u'جامعة الملك فيصل'),
    ('KSAU' ,u'جامعة الملك سعود'),
    ('PSU' ,u'جامعة الأمير سلطان'),
    ('KSU' , u'جامعة الملك سلمان الخرج'),
    )
blocks_choices= (
    ('FB',u'Foundation Block'),
    ('MSK',u'Musculoskeletal Block'),
    ('R',u'Respiratory Block'),
    ('HT',u'Hematology Block'),
    ('CV',u'Cardiovascular Block'),
    ('NS',u'Neurosciences Block'),
    ('EC',u'Endocrine Block'),
    ('UR',u'Urology and Renal Block'),
    ('GIT',u'Gastroenterology Block'),
    ('O',u'Oncology Block'),
    ('EBM',u'EBM Block'),
    ('FM',u'Family Medicine block'),
    ('M',u'Medicine Block'),
    ('P',u'Pediatric Block'),
    ('S',u'Surgery Block'),
    ('OBGN',u'Obstetrics and Gynecology Block'),
    ('SSMH',u'Special Sense & Mental Health Block Book'))
rating_choices=(
    ('5',u'5 Stars out of 5'),
    ('4',u'4 Stars out of 5'),
    ('3',u'3 Stars out of 5'),
    ('2',u'2 Stars out of 5'),
    ('1',u'1 Stars out of 5'),
)
clinical_choices=(
    ('Yes',u'It is clinical'),
    ('NO',u'It is not clinical')
)
comment_choices=(
    ('Yes',u'It is clinical'),
    ('NO',u'It is not clinical')
)
class College(models.Model):
    name = models.CharField(max_length=1, choices=college_choices, verbose_name=u"الاسم")
    city = models.CharField(max_length=1, choices=city_choices, verbose_name=u"المدينة")
    gender = models.CharField(max_length=1, choices=gender_choices, verbose_name=u"الجنس")

class Profile(models.Model):
    user = models.OneToOneField(User,
                                unique=True,
                                related_name='profile')

    is_student = models.BooleanField(default=True,
                                     verbose_name=u"طالب؟")
    ar_first_name = models.CharField(max_length=30,
                                     verbose_name=u'الاسم الأول')
    ar_last_name = models.CharField(max_length=30,
                                    verbose_name=u'الاسم الأخير')
    en_first_name = models.CharField(max_length=30,
                                     verbose_name=u'الاسم الأول')
    en_last_name = models.CharField(max_length=30,
                                    verbose_name=u'الاسم الأخير')
    city = models.CharField(max_length=1, choices=city_choices, verbose_name=u"المدينة")

    gender = models.CharField(max_length=1, choices=gender_choices,
                              verbose_name=u"الجنس", blank=True,
                              default="")
    university = models.CharField (max_length=1, choices=university_choics, verbose_name=u"الجامعة")

    college = models.ForeignKey(College, null=True,
                                blank=True,
                                on_delete=models.SET_NULL,
                                verbose_name=u'الكلية')
    batch = models.PositiveSmallIntegerField(verbose_name=u'الدفعة')
    profile_picture = models.FileField(upload_to='profile_pics', blank=True, null=True)
class Block (models.Model):
    title = models.CharField(max_length=120, verbose_name=u'اسم البلوك ')
    cover = models.ImageField("صورة البلوك",default='http://riddim-donmagazine.com/wp-content/uploads/2015/12/Concrete-Block.jpg')
    is_clinical = models.BooleanField(u'is the block clinical?',default=False)
    description = models.TextField(verbose_name=u"وصف البلوك", blank=True, help_text=u"اختياري")
    def __str__(self):
        return self.title
class Category(models.Model):
    name = models.CharField(max_length=100)
    block = models.ManyToManyField(Block, blank=True,default='block.id')
    cover = models.ImageField("صورة التصنيف",null=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('m9adery:categorybooks', kwargs={'pk':self.pk})
class Book (models.Model):
    title = models.CharField(max_length=120,verbose_name=u'اسم الكتاب')
    description = models.TextField(verbose_name=u"وصف الكتاب", blank=True, help_text=u"اختياري")
    submitter = models.ForeignKey(User, null=True,
                                  on_delete=models.SET_NULL,
                                  related_name='book_contributions')

    #cover = models.CharField(max_length=1000,blank=True,default='http://www.danieladorno.com/wp-content/uploads/2014/04/Empty_book_cover.png',verbose_name=u'غلاف الكتاب')
    cover = models.ImageField("صورة الكتاب")

    download = models.CharField(max_length=250,verbose_name=u'رابط التحميل',blank=True, help_text=u"اختياري")

    submission_date = models.DateTimeField(u"تاريخ الرفع",
                                           auto_now_add=True)
    category = models.ManyToManyField(Category,blank=True, help_text=u"اختياري")
    block = models.ManyToManyField(Block,blank=True, help_text=u"اختياري")
    def get_absolute_url(self):
        return reverse('m9adery:bookdetail', kwargs={'pk':self.pk})
    def __str__(self):
        return self.title
class Comment (models.Model):
    submitter = models.ForeignKey(User, null=True,
                                  on_delete=models.SET_NULL,)
    description = models.TextField(verbose_name=u"وصف التقييم", blank=True, help_text=u"اختياري")
    submission_date = models.DateTimeField(u"تاريخ الاضافة",
                                           auto_now_add=True)
    rating = models.CharField(max_length=1, choices=rating_choices)
    books = models.ForeignKey(Book,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.submitter)+'  -   '+self.description+'  -  '+str(self.books)
class CommentRating (models.Model):
    submitter = models.ForeignKey(User, null=True,
                                  on_delete=models.SET_NULL, )
    is_positive=models.BooleanField()
    rating = models.PositiveSmallIntegerField()