from django.contrib import admin

# Register your models here.


from labour_management_system.models import District, Person, Bank_Details, Supervisor

admin.site.register(District)
admin.site.register(Person)
admin.site.register(Bank_Details)
admin.site.register(Supervisor)

