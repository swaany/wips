from django import forms
from .models import BlockLog

class PostForm(forms.ModelForm):
	class Meta:
		model = BlockLog
		fields = ('block_stat',)