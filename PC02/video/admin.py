from django.contrib import admin

# Register your models here.
from .models import TipoDeVideo
admin.site.register(TipoDeVideo)

from .models import Alquiler
admin.site.register(Alquiler)

from .models import Cliente
admin.site.register(Cliente)