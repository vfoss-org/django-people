"""Admin classes for the ``people`` app."""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from hvad.admin import TranslatableAdmin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from . import settings
from . import models
from .forms import LinkTypeForm


class NationalityAdmin(TranslatableAdmin):
    """Admin for the ``Nationality`` model."""
    list_display = ['get_name', 'all_translations']
    list_select_related = []

    def get_name(self, obj):
        return obj.name
    get_name.short_description = _('Name')


class LinkAdmin(admin.ModelAdmin):
    """Admin for the ``Link`` model."""
    list_display = ['person', 'link_type', 'url', ]


class LinkInline(admin.TabularInline):
    """Inline admin for ``Link`` objects."""
    model = models.Link


class LinkTypeAdmin(TranslatableAdmin):
    """Admin for the ``LinkType`` model."""
    form = LinkTypeForm
    list_display = ['get_name', 'ordering', 'all_translations', ]
    list_select_related = []

    class Meta:
        model = models.LinkType

    def get_name(self, obj):
        return obj.name
    get_name.short_description = _('Name')

class ProfileInline(admin.StackedInline):
    model = models.Person
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

#class CustomUserAdmin(UserAdmin):
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class PersonAdmin(TranslatableAdmin):
    """Admin for the ``Person`` model."""
    inlines = [LinkInline, ]
    readonly_fields = ['user']
    list_display = [
        'username', # django.auth.User
        'roman_first_name', 'roman_last_name', 'non_roman_first_name_link',
        'non_roman_last_name', 'chosen_name', 'gender', 'title', 'role',
        'phone', 'email', 'ordering', 'all_translations', ]
    search_fields = [
        'user__username',
        'roman_first_name','roman_last_name', 'email', ]
    list_select_related = [] # ['user',] not implemented by hvad
    #list_filter = [ 'user__is_staff' ]

    def non_roman_first_name_link(self, obj):
        return u'<a href="{0}/">{1}</a>'.format(
            obj.pk, obj.non_roman_first_name)
    non_roman_first_name_link.allow_tags = True
    non_roman_first_name_link.short_description = "Non roman first name"


class RoleAdmin(TranslatableAdmin):
    """Admin for the ``Role`` model."""
    list_display = ['get_name', 'all_translations', ]
    list_select_related = []

    def get_name(self, obj):
        return obj.name
    get_name.short_description = _('Name')


admin.site.register(models.Nationality, NationalityAdmin)
admin.site.register(models.Link, LinkAdmin)
admin.site.register(models.LinkType, LinkTypeAdmin)
admin.site.register(models.Person, PersonAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(models.Role, RoleAdmin)
