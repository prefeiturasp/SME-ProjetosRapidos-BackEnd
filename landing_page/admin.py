from django.contrib import admin
from django import forms
from landing_page.models import Section


class SectionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SectionForm, self).__init__(*args, **kwargs)
        self.fields['body'].help_text = 'Se for uma listagem, separe usando ";".'

    class Meta:
        model = Section
        exclude = ()

class MyModelAdmin(admin.ModelAdmin):
    form = SectionForm


admin.site.register(Section, MyModelAdmin)
