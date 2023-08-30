from django.contrib import admin


from .models import Train, Station, TrainClass
# Register your models here.
admin.site.register(Train)
admin.site.register(Station)
admin.site.register(TrainClass)

