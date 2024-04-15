from django.apps import AppConfig
from django.conf import settings
class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"
    #MAKING USER DEFAULT USER AUTOMATICALLY
    def ready(self):
        from django.contrib.auth.models import Group
        from django.db.models.signals import post_save

        def add_to_default_group(sender , **kwargs):
            #THE CURRENT USER JUST REGISTERED
            user = kwargs['instance']
            if kwargs['created']:
                group,ok = Group.objects.get_or_create(name='default')
                #ADD THE USER TO DEFAUL
                group.user_set.add(user)
        #WHEN USER REGISTER IT CALL THIS
        post_save.connect(add_to_default_group,sender=settings.AUTH_USER_MODEL)
