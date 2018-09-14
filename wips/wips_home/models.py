from django.db import models
from django.utils import timezone

# Create your models here.

class BlockLog(models.Model):
	number = models.AutoField(primary_key = True)
	mac = models.CharField(max_length=12)
	block_pkt = models.FileField()
	atk_type = models.TextField()
	pkt_time = models.DateTimeField(blank=True, null=True)
	block_stat = models.BooleanField(blank=True, default='False')

	object = models.Manager()


	def __str__(self):
		return self.atk_type
		
