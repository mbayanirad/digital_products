from secrets import choice
from tabnanny import verbose
from turtle import title, update
from unicodedata import category
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Category(models.Model):
    parent = models.ForeignKey('self',verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_("avatar"), upload_to='categories/',blank=True)
    isEnable = models.BooleanField(_('is enable'), default=True)
    createdTime = models.DateTimeField(_('created time'), auto_now_add=True)
    updateTime = models.DateTimeField(_('update time'), auto_now_add=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_("avatar"), upload_to='products/',blank=True)
    isEnable = models.BooleanField(_('is enable'), default=True)
    categories = models.ManyToManyField('Category', verbose_name=_('categories'), blank=True)
    createdTime = models.DateTimeField(_('created time'), auto_now_add=True)
    updateTime = models.DateTimeField(_('update time'), auto_now_add=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('meysamn')
        verbose_name_plural = _('mey=samssssss')
   
    def __str__(self):
        return self.title

class File(models.Model):
    FILE_AUDIO = 1
    FILE_VIDEO = 2
    FILE_PDF = 3
    FILE_TYPE = (
            (FILE_AUDIO, _('audio')),
            (FILE_VIDEO, _('video')),
            (FILE_PDF, _('pdf'))
    )

    product = models.ForeignKey('Product', related_name='files', verbose_name=_('products'), blank=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    fileType = models.PositiveSmallIntegerField(_("file type"), choices=FILE_TYPE)
    file = models.FileField(_('file'), upload_to='files/%Y/%m/%d/')
    isEnable = models.BooleanField(_('is enable'), default=True)
    createdTime = models.DateTimeField(_('created time'), auto_now_add=True)
    updateTime = models.DateTimeField(_('update time'), auto_now_add=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')
 
    def __str__(self):
        return self.title
