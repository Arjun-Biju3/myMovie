from django.contrib import admin
from Movies.models import Movies,MovieComments,MovieReview,Genere

admin.site.register(Movies)
admin.site.register(MovieComments)
admin.site.register(MovieReview)
admin.site.register(Genere)
