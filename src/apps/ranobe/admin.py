from django.contrib import admin

from apps.ranobe.models import Ranobe, RanobeChapter, RanobeText, RanobeVolume


class RanobeVolumeInline(admin.TabularInline):
    model = RanobeVolume
    extra = 0


class RanobeChapterInline(admin.TabularInline):
    model = RanobeChapter
    extra = 0


class RanobeTextInline(admin.TabularInline):
    model = RanobeText
    extra = 0


@admin.register(Ranobe)
class RanobeAdmin(admin.ModelAdmin):
    list_display = ("__str__", "volume_amount",)
    search_fields = ("composition__name",)
    list_filter = ("status",)
    inlines = (RanobeVolumeInline,)


@admin.register(RanobeVolume)
class RanobeVolumeAdmin(admin.ModelAdmin):
    list_display = ("name", "chapter_amount",)
    search_fields = ("name",)
    inlines = (RanobeChapterInline,)


@admin.register(RanobeChapter)
class RanobeChapterAdmin(admin.ModelAdmin):
    list_display = ("name_ranobe", "name",)
    search_fields = ("name",)
    inlines = (RanobeTextInline,)


@admin.register(RanobeText)
class RanobeTextAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("translation",)
