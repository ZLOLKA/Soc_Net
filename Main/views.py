from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms
from . import models


# Create your views here.
def home(request):
    persons = models.Person.objects.all()           # SELECT * FROM Person;
    vk_accs = models.VK_acc.objects.all()           # SELECT * FROM VK_acc;
    vk_net = models.VK_net.objects.all()            # SELECT * FROM VK_net;
    vk_groups = models.VK_group.objects.all()       # SELECT * FROM VK_group;
    inst_accs = models.Instagram_acc.objects.all()  # SELECT * FROM Instagram_acc;
    inst_net = models.Instagram_net.objects.all()   # SELECT * FROM Instagram_net;
    context = {
        "persons": persons,
        "vk_accs": vk_accs,
        "vk_net": vk_net,
        "vk_groups": vk_groups,
        "inst_accs": inst_accs,
        "inst_net": inst_net,
    }
    return render(request, "Home.html", context)

def db_form(request, table_name):
    if table_name == "Person":
        Form = forms.PersonForm
    elif table_name == "VK_acc":
        Form = forms.VK_accForm
    elif table_name == "VK_net":
        Form = forms.VK_netForm
    elif table_name == "VK_group":
        Form = forms.VK_groupForm
    elif table_name == "Instagram_acc":
        Form = forms.Instagram_accForm
    elif table_name == "Instagram_net":
        Form = forms.Instagram_netForm
    else:
        raise Exception("Incorrect table name")

    form = Form()
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    context = {
        "form": form,
    }
    return render(request, "DB_Form.html", context)
