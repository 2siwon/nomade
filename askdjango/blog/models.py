from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목',
        help_text='포스팅 제목을 입력해주세요. 최대 100자 내외') # 길이 제한이 있는 문자열
    content = models.TextField()             # 길이 제한이 없는 문자열
    created_at = models.DateTimeField(auto_now_add=True) # 최초만
    updated_at = models.DateTimeField(auto_now=True)     # 업데이트 마다 자동저장

    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True, help_text='위도/경도 포맷으로 입력')