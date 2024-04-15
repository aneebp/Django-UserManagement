from django import template

register = template.Library()

@register.filter
def has_delete_permission(user):
    return user.has_perm("main.delete_post")
