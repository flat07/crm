from django.contrib import admin

from .models import (
    Deal,
    DealCompetitor,
    DealProduct,
    DealStageHistory,
)

admin.site.register(Deal)
admin.site.register(DealStageHistory)
admin.site.register(DealCompetitor)
admin.site.register(DealProduct)
