from django.shortcuts import render

from .models import FeedBack

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