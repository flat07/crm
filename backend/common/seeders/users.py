# staff/seeders/users.py

from staff.models import Department, Role, User

USERS = [
    {
        "email": "admin@a.com",
        "first_name": "Admin",
        "last_name": "User",
        "department": "Administration",
        "role": "Administrator",
        "is_superuser": True,
    },
    {
        "email": "manager@a.com",
        "first_name": "Sales",
        "last_name": "Manager",
        "department": "Sales",
        "role": "Sales Manager",
        "is_superuser": False,
    },
    {
        "email": "support@a.com",
        "first_name": "Support",
        "last_name": "Agent",
        "department": "Support",
        "role": "Support",
        "is_superuser": False,
    },
    {
        "email": "marketing@a.com",
        "first_name": "Marketing",
        "last_name": "User",
        "department": "Marketing",
        "role": "Marketing",
        "is_superuser": False,
    },
]


def seed_users(command):

    for data in USERS:
        department = Department.objects.get(name=data["department"])
        role = Role.objects.get(name=data["role"])

        user, _ = User.objects.get_or_create(
            email=data["email"],
            defaults={
                "first_name": data["first_name"],
                "last_name": data["last_name"],
                "department": department,
                "is_staff": True,
                "is_superuser": data["is_superuser"],
            },
        )

        # Keep the seed data in sync even if it already exists.
        user.first_name = data["first_name"]
        user.last_name = data["last_name"]
        user.department = department
        user.is_staff = True
        user.is_superuser = data["is_superuser"]

        # Password is always "admin"
        user.set_password("admin")
        user.save()

        # Replace any existing roles with the seeded role.
        user.roles.set([role])

    command.stdout.write(command.style.SUCCESS(f"✓ Seeded {len(USERS)} users"))
