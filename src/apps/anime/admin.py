from django.contrib import admin

from apps.anime.models import Anime, AnimeSeason, AnimeSeries, AnimeVideo


class AnimeSeasonInline(admin.TabularInline):
    model = AnimeSeason
    extra = 0


class AnimeSeriesInline(admin.TabularInline):
    model = AnimeSeries
    extra = 0


class AnimeVideoInline(admin.TabularInline):
    model = AnimeVideo
    extra = 0


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ("__str__", "season_amount")
    search_fields = ("composition__name",)
    inlines = (AnimeSeasonInline,)


@admin.register(AnimeSeason)
class AnimeSeasonAdmin(admin.ModelAdmin):
    list_display = ("name", "number", "series_amount")
    search_fields = ("anime__composition__name",)
    inlines = (AnimeSeriesInline,)


@admin.register(AnimeSeries)
class AnimeSeriesAdmin(admin.ModelAdmin):
    list_display = ("name_anime", "name_series", "number",)
    search_fields = ("name",)
    inlines = (AnimeVideoInline,)


@admin.register(AnimeVideo)
class AnimeVideoAdmin(admin.ModelAdmin):
    list_display = ("name_series",)
