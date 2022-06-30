from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView,View, UpdateView, DeleteView
from newsletters.models import Newsletter
from .forms import NewsletterCreationForm
from django.core.mail import send_mail, EmailMessage
# Create your views here.
class DashboardHomeView(TemplateView):
    template_name = 'dashboard/index.html'
    
class NewslettersDashboardHomeView(View):
    def get(self, request, *args, **kwargs):
        newsletters= Newsletter.objects.all()
        context ={
            'newsletters':newsletters,
        }
        return render(request,'dashboard/list.html',context)

class NewslettersCreateView(View):
    def get(self, request, *args, **kwargs):
        form = NewsletterCreationForm()
        context = {
            'form':form
        }
        return render(request, 'dashboard/create.html',context)
    
    def post(self,request, *args, **kwargs):
        if request.method=='POST':
            form =NewsletterCreationForm(request.POST or None)
            if form.is_valid():
                instance = form.save()
                newsletter = Newsletter.objects.get(id=instance.id)
                if newsletter.status == 'Published':
                    subject = newsletter.subject
                    body = newsletter.body
                    from_email = settings.EMAIL_HOST_USER
                    for email in newsletter.email.all():
                        send_mail(subject=subject, from_email=from_email, recipient_list=[email], message=body, fail_silently=True)
                return redirect('dashboard:list')
        context ={
            'form':form
        }
        return render(request, 'dashboard/create.html',context)

class NewsletterDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        newsletter = get_object_or_404(Newsletter,pk=pk)
        context = {
            'newsletter':newsletter,
        }  
        return render(request, 'dashboard/detail.html',context)


class NewslettersUpdateView(UpdateView):
    model = Newsletter
    form_class = NewsletterCreationForm
    template_name = 'dashboard/update.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type':'update'
        })
        return context
    def post(self, request, pk, *args, **kwargs):
        object= super().post(request, *args, **kwargs)
        newsletter = Newsletter.objects.get(id=pk)
        if newsletter.status == 'Published':
            subject = newsletter.subject
            body = newsletter.body
            from_email = settings.EMAIL_HOST_USER
            for email in newsletter.email.all():
                send_mail(subject=subject, from_email=from_email, recipient_list=[email], message=body, fail_silently=True)
        return object


    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('dashboard:detail', kwargs={'pk':pk})
    

class NewsletterDeleteView(DeleteView):
    model = Newsletter
    template_name = 'dashboard/delete.html'
    success_url = reverse_lazy('dashboard:list')
