from django.contrib import admin
from series.models import Series,SeriesComments,SeriesReview,Trailer,Season

admin.site.register(Series)
admin.site.register(SeriesComments)
admin.site.register(SeriesReview)
admin.site.register(Trailer)
admin.site.register(Season)
