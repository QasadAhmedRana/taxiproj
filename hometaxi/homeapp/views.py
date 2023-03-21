from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice, Anfrage
from django.views import generic
from django.utils import timezone
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'homeapp/index.html'


    def get_queryset(self):
         """
    Return the last five published questions (not including those set to be
    published in the future).
    """
         return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy

# contact/views.py

class ContactView(FormView):
    template_name = 'homeapp/contact.html'
   # template_name = 'contact/send_mail.html'
    form_class = ContactForm
    success_url = reverse_lazy('homeapp:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)


# contact/views.py
class ContactSuccessView(TemplateView):
    template_name = 'homeapp/success.html'

class InnerPageView(TemplateView):
    template_name = 'inner-page.html'

#Datenschutz view
def datenschutz(request):
    return render(request, 'homeapp/datenschutz.html')

