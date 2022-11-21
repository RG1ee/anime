from src.apps.achievements.models import Achievement


def add_welcome_achievement(sender, instance, created: bool, **kwargs):
    if created:
        achievement, created = Achievement.objects.get_or_create(
            name="Student of the academy", description="Welcome to the website"
        )
        instance.achievement.add(achievement)
