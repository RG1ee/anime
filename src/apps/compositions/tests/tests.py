import pytest

from src.apps.compositions.models import Composition


@pytest.mark.django_db
def test_model():
    Composition.objects.create(
        name="Naruto", description="lala", image="123.jpg"
    )
    assert Composition.objects.count() == 1
