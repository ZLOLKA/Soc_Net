from django.shortcuts import render
from . import models


# Create your views here.
def home(request):
    persons = models.Person.objects.all()
    vk_accs = models.VK_acc.objects.all()
    vk_net = models.VK_net.objects.all()
    vk_groups = models.VK_group.objects.all()
    inst_accs = models.Instagram_acc.objects.all()
    inst_net = models.Instagram_net.objects.all()
    context = {
        "persons": persons,
        "vk_accs": vk_accs,
        "vk_net": vk_net,
        "vk_groups": vk_groups,
        "inst_accs": inst_accs,
        "inst_net": inst_net,
    }
    return render(request, "Home.html", context)
