from site_vetclinic.models import Service, User, GroupService
from django.views.generic import TemplateView, ListView, DeleteView, DetailView



class IndexTemplate(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['group_services'] = GroupService.objects.all()
        context['doctors'] = User.objects.filter(groups__name='Ветеринарный врач')
        return self.render_to_response(context)


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

class DoctorTemplate(DetailView):
    model = User
    template_name = "doctors/item.html"

class Authentication(TemplateView):
    template_name = "authentication/login.html"

class Registration(TemplateView):
    template_name = "registration.html"

class ServiceTemplate(DetailView):
    model = GroupService
    template_name = "services/item.html"

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {}
        if self.object:
            context["object"] = self.object
            context["services"] = Service.objects.filter(group__pk=self.object.pk)
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super().get_context_data(**context)



class ServicesTemplate(ListView):
    model = GroupService
    template_name = "services/services.html"
