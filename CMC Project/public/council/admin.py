from django.contrib import admin

from council.models import *
# from council.models import 

# Register your models here.
admin.site.register(state)
admin.site.register(district)
admin.site.register(taluk)
admin.site.register(City)
admin.site.register(ward_noo)
admin.site.register(colony)
# admin.site.register(water)
admin.site.register(Complaints)
admin.site.register(members)
admin.site.register( WardMember)
