from django.db import models
from django import forms
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
import re
from monday.utils import random_name_upload_to
# Create your models here.
def min_length_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력하시오.')

# 폰필드 1
# class PhoneField(models.CharField):
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault('max_length', 11)
#         super(PhoneField, self).__init__(*args, **kwargs)
#         validator = RegexValidator(r'^01[016789]\d{7,8}$',
#             message='휴대폰 번호를 입력해주세요.')
#         self.validators.append(validator)


# 폰필드 2
# def phone_validator(value):
#     number = ''.join(re.findall(r'\d+', value))
#     return RegexValidator(r'^01[016789]\d{7,8}$', message = '휴대폰 번호를 입력해 주세요,')(number)


# class PhoneField(models.CharField):
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault('max_length', 20)
#         super(PhoneField, self).__init__(*args, **kwargs)
#         self.validators.append(phone_validator)


# 폰필드 3
def phone_validator(value):
    number = ''.join(re.findall(r'\d+', value))
    if not re.match(r'^01[016789]\d{7,8}$', number):
        raise forms.ValidationError('휴대폰 번호를 입력해 주세요.')


class PhoneField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 20)
        super(PhoneField, self).__init__(*args, **kwargs)
        self.validators.append(phone_validator)


class Post(models.Model):
    title = models.CharField(max_length = 100,
            validators = [min_length_validator],
            help_text = "100자 이내로 입력하세요.")
    content = models.TextField()
    phone = PhoneField(blank = True)
    photo = models.ImageField(blank = True, upload_to = random_name_upload_to)
    tags = models.ManyToManyField('Tag', blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.pk])


class Tag(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey('Post')
    title = models.TextField()

    def __str__(self):
        return self.title

