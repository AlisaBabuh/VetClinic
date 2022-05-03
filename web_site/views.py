from site_vetclinic.models import User
from django.views.generic import TemplateView, ListView, DeleteView


class IndexTemplate(TemplateView):
    template_name = "index.html"

class AboutTemplate(TemplateView):
    template_name = "about.html"

class ContactsTemplate(TemplateView):
    template_name = "contacts.html"

class DoctorsTemplate(ListView):
    model = User
    template_name = "doctors/doctors.html"

    def get_queryset(self):
        doctors = User.objects.filter(groups__name='Ветеринарный врач')
        return doctors

class DoctorTemplate(DeleteView):
    model = User
    template_name = "doctors/item.html"

    def get_queryset(self):
        doctors = User.objects.filter(groups__name='Ветеринарный врач')
        return doctors

class ServicesTemplate(TemplateView):
    template_name = "services.html"

class AbgalinaTemplate(TemplateView):
    template_name = "abgalina.html"

class AnalizTemplate(TemplateView):
    template_name = "analiz.html"