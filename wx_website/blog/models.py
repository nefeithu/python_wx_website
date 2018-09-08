# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 150, verbose_name='文章标题')  # blog title
    category = models.CharField(max_length = 50, blank= True, verbose_name='文章标签')
    pub_date = models.DateTimeField(auto_now_add = True, editable = True, verbose_name='发布时间')
    update_time = models.DateTimeField(auto_now_add = True, null = True, verbose_name='更新时间')
    content = models.TextField(blank = True, null = True, verbose_name='文章内容')
    
    def __str__(self):
        return self.title
    
    class Meta:
        #按发布时间降序排列
        ordering = ['-pub_date']
        verbose_name = '文章'
        verbose_name_plural = '文章'
        
