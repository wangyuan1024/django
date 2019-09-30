# -*- coding: UTF-8 -*-
##########################################################################
# File Name: forms.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年09月19日 星期四 14时50分52秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

from  django import forms
from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = {'text'}
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
