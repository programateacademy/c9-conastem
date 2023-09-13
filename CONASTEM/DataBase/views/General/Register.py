from django.http import HttpResponse
from django.views import generic
from ...models.Register import Register

class RegisterListView(generic.ListView):
    model = Register
    context_object_name= 'register_list'
    # queryset= Register.objects.all().filter(Register.institution_name)
    template_name= 'records.html'

class RegisterListDetail(generic.DetailView):
    model = Register
    context_object_name = 'register_detail'
    template_name= 'records_detail.html'
    