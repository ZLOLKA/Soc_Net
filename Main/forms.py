from django import forms
from . import models


class PersonForm(forms.ModelForm):
    """
INSERT INTO Person (
    first_name,
    last_name,
    patronymic,
    birth_year,
    birth_month,
    birth_day,
    mob_number
) VALUES (
    get_from_form_first_name,
    get_from_form_last_name,
    get_from_form_patronymic,
    get_from_form_birth_year,
    get_from_form_birth_month,
    get_from_form_birth_day,
    get_from_form_mob_number
);
    """
    class Meta:
        model = models.Person
        fields = "__all__"


class VK_accForm(forms.ModelForm):
    """
INSERT INTO Vk_acc (
    city,
    school,
    university,
    id_person
) VALUES (
    get_from_form_city,
    get_from_form_school,
    get_from_form_university,
    get_from_form_id_person
);
    """
    class Meta:
        model = models.VK_acc
        fields = "__all__"


class Vk_netForm(forms.ModelForm):
    """
INSERT INTO VK_net (
    who,
    on_whom
) VALUES (
    get_from_form_who,
    get_from_form_on_whom
);
    """
    class Meta:
        model = models.VK_net
        fields = "__all__"


class Vk_groupForm(forms.ModelForm):
    """
INSERT INTO Vk_group (
    id,
    name
) VALUES (
    get_from_form_id,
    get_from_form_name
);
    """
    class Meta:
        model = models.VK_group
        fields = "__all__"


class Instagram_accForm(forms.ModelForm):
    """
INSERT INTO Instagram_acc (
    id_person
) VALUES (
    get_from_form_id_person
);
    """
    class Meta:
        model = models.Instagram_acc
        fields = "__all__"


class Instagram_net(forms.ModelForm):
    """
INSERT INTO Instagram_net (
    who,
    on_whom
) VALUES (
    get_from_form_who,
    get_from_form_on_whom
);
    """
    class Meta:
        model = models.Instagram_net
        fields = "__all__"
