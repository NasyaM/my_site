from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

def feedback_list(request):
       if request.method == "POST":
           form = FeedbackForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('feedback:feedback_list')  # Замените 'feedback:feedback_list' на ваш URL.

       else:
           form = FeedbackForm()

       verified_feedbacks = Feedback.objects.filter(is_verified=True)

       return render(request, 'feedback/feedback_list.html', {
           'form': form,
           'feedbacks': verified_feedbacks,
       })