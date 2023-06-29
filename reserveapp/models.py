from django.conf import settings
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils import timezone


class Room(models.Model):
    floor = models.IntegerField(blank=False, verbose_name='층수')
    name = models.CharField(max_length=10, verbose_name='회의실 이름')
    max_capacity = models.PositiveSmallIntegerField(verbose_name='최대 수용 인원')

    def __str__(self):
        # return f"Custom Post object ({self.id})"
        return self.name


class ReservedRoom(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='예약자'
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        verbose_name='회의실 ID'
    )
    reserved_date = models.DateField(verbose_name='예약일')
    started_at = models.TimeField(verbose_name='예약 시작 시간')
    finished_at = models.TimeField(verbose_name='예약 종료 시간')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        # return f"Custom Post object ({self.id})"
        return self.room.name

    def get_absolute_url(self):  # redirec 할 때 굉장히 편리해진다.
        return reverse('reserveapp:reservedroom_detail', args=[self.pk])

    def clean(self):
        if self.reserved_date < timezone.now().date():
            raise ValidationError('예약일은 오늘 이전으로 설정할 수 없습니다.')

        if self.finished_at and self.started_at >= self.finished_at:
            raise ValidationError('예약 시작 시간은 예약 종료 시간보다 이전이어야 합니다.')
