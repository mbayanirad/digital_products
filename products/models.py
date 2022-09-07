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
    avatar = models.models.ImageField(_("avatar"), upload_to='categories/',blank=True)
    isEnable = models.BooleanField(_('is enable'), default=True)
    createdTime = models.DateTimeField(_('created time'), auto_now_add=True)
    updateTime = models.DateTimeField(_('update time'), auto_now_add=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

class Product(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.models.ImageField(_("avatar"), upload_to='products/',blank=True)
    isEnable = models.BooleanField(_('is enable'), default=True)
    categories = models.ManyToManyField(_('Category'), verbose_name=_('categories'), blank=True)
    createdTime = models.DateTimeField(_('created time'), auto_now_add=True)
    updateTime = models.DateTimeField(_('update time'), auto_now_add=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')


class File(models.Model):
    product = models.ForeignKey('Product', verbose_name=_('products'), blank=True)
    title = models.CharField(_('title'), max_length=50)
    file = models.FileField(_('file'), upload_to='files/%Y/%m/%d/')
    isEnable = models.BooleanField(_('is enable'), default=True)
    createdTime = models.DateTimeField(_('created time'), auto_now_add=True)
    updateTime = models.DateTimeField(_('update time'), auto_now_add=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')
 
