from django.http import HttpResponseRedirect
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

def db_form(request, table_name):
    if table_name == "Course":
        Form = CourseForm
    elif table_name == "Teacher":
        Form = TeacherForm
    elif table_name == "Class":
        Form = ClassForm
    elif table_name == "Student":
        Form = StudentForm
    elif table_name == "Level":
        Form = LevelForm
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
