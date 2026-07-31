# staff/seeders/departments.py

from staff.models import Department

DEPARTMENTS = [
    "Administration",
    "Sales",
    "Support",
    "Marketing",
]


def seed_departments(command):

    for name in DEPARTMENTS:
        Department.objects.update_or_create(
            name=name,
        )

    command.stdout.write(command.style.SUCCESS("✓ Departments seeded"))
