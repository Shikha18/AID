from django.contrib import admin
from .models import yojna_desc,Field,state,problem,yojna_state,yojna_problem

admin.site.register(yojna_desc)
admin.site.register(Field)
admin.site.register(state)
admin.site.register(problem)
admin.site.register(yojna_state)
admin.site.register(yojna_problem)