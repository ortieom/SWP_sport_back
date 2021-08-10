from datetime import date

import pytest
from django.contrib.auth import get_user_model

from sport.models import Student
from sport.models import MedicalGroups
from api.crud import get_email_name_like_students


User = get_user_model()


@pytest.mark.django_db
def test_student_create(student_factory):
    student_factory("A@foo.bar")
    assert User.objects.count() == 1
    assert Student.objects.count() == 1


@pytest.mark.django_db
def test_student_delete(student_factory):
    student_user = student_factory("A@foo.bar")
    assert User.objects.count() == 1
    assert Student.objects.count() == 1
    student_user.delete()
    assert User.objects.count() == 0
    assert Student.objects.count() == 0


@pytest.mark.django_db
def test_get_email_name_like_students(
        student_factory,
        semester_factory,
        sport_factory,
        group_factory
):
    user = student_factory(
        first_name="Kirill",
        last_name="Fedoseev",
        email="k.fedoseev@innopolis.university",
    )
    assert get_email_name_like_students(0, "Kirill") == [{
        "id": user.student.pk,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "full_name": f"{user.first_name} {user.last_name}",
    }]
    assert len(get_email_name_like_students(0, "Kir")) == 1
    assert len(get_email_name_like_students(0, "Kirill Fed")) == 1
    assert len(get_email_name_like_students(0, "Kirill Fedoseev")) == 1
    assert len(get_email_name_like_students(0, "k.fedoseev")) == 1
    assert len(
        get_email_name_like_students(0,"k.fedoseev@innopolis.university")
    ) == 1
    assert len(get_email_name_like_students(0, "kfedoseev")) == 0

    start = date(2020, 1, 20)
    end = date(2020, 1, 27)
    sem = semester_factory(
        name="S20",
        start=start,
        end=end,
    )

    sport = sport_factory(
        name="football",
        special=False,
    )

    group = group_factory(
        name="F-S20-01",
        capacity=30,
        sport=sport,
        semester=sem,
    )
    assert len(
        get_email_name_like_students(
            group.id,
            "k.fedoseev@innopolis.university"
        )
    ) == 1
    group.allowed_medical_groups = [
        MedicalGroups.GENERAL,
        MedicalGroups.PREPARATIVE,
        MedicalGroups.SPECIAL1,
    ]
    group.save()
    assert len(
        get_email_name_like_students(
            group.id,
            "k.fedoseev@innopolis.university"
        )
    ) == 0
    user.student.medical_group_id = 0
    user.save()
    assert len(
        get_email_name_like_students(
            group.id,
            "k.fedoseev@innopolis.university"
        )
    ) == 1
