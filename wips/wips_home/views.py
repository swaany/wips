from wips_home.models import BlockLog
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from wips_home.forms import PostForm


def base(request):
    return render(request, 'wips_home/base.html', {})


def block_list(request):
	BlockLogS = BlockLog.object.all()
	return render(request, 'wips_home/block_list.html',{'BlockLogS':BlockLogS})

#def block_list(request, pk):
 #   post = get_object_or_404(Post, pk=pk)
  #  return render(request, 'wips_home/block_list.html', {'post': post})


# Create your views here.
def block_list_post(request,pk):
	bpost = get_object_or_404(BlockLog, pk=pk)
	if request.method=="POST":
		form = PostForm(request.POST, instance=bpost)
		if form.is_valid():
			bpost=form.save()
			return redirect(request.path_info)

		else:
			form = PostForm(instance=bpost)

		return render(request, 'wips_home/block_list_post.html',{'BlockLog':bpost, 'form':form})
		