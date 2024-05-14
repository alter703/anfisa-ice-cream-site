from django.shortcuts import render
from django.shortcuts import render, redirect

from .models import FeedBack
from .forms import FeedBackForm

# Create your views here.
def index(request):
    # return render(request, 'feedback/index.html')

    template = 'feedback/feedback_list.html'
    feedbacks = FeedBack.objects.all() 

    # # только то мороженое, у кторого есть флаг on_main
    context = {
        'feedbacks': feedbacks,
    }
    return render(request, template, context)

def publish_feedback(request):
    context = {
        'created_form': FeedBackForm()
    }

    return render(request, 'feedback/feedback_publish.html', context)


def feedback(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.author = request.user
            feedback.save()
            return redirect('feedback:feedback_list')
    else:
        form = FeedBackForm()
    return render(request, 'feedback/feedback_publish.html', {'form': form})

