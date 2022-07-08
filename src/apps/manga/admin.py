from django.contrib import admin

from apps.manga.models import Manga, MangaChapter, MangaImage, MangaVolume


class MangaVolumeInline(admin.TabularInline):
    model = MangaVolume
    extra = 0


class MangaChapterInline(admin.TabularInline):
    model = MangaChapter
    extra = 0


class MangaImageInline(admin.TabularInline):
    model = MangaImage
    extra = 0


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ("__str__", "volume_amount",)
    search_fields = ("composition__name",)
    list_filter = ("translation",)
    inlines = (MangaVolumeInline,)


@admin.register(MangaVolume)
class MangaVolumeAdmin(admin.ModelAdmin):
    list_display = ("composition_name", "number", "chapter_amount")
    inlines = (MangaChapterInline,)


@admin.register(MangaChapter)
class MangaChapterAdmin(admin.ModelAdmin):
    list_display = ("name_manga", "name", "page_amount",)
    search_fields = ("name",)
    inlines = (MangaImageInline,)


@admin.register(MangaImage)
class MangaImageAdmin(admin.ModelAdmin):
    list_display = ("name_manga", "chapter_name", "number",)
