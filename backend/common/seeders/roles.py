# staff/seeders/roles.py

from staff.models import Permission, Role

ROLE_PERMISSIONS = {
    "Administrator": "__all__",
    "Sales Manager": [
        "dashboard.view",
        "company.view",
        "company.create",
        "company.update",
        "contact.view",
        "contact.create",
        "contact.update",
        "lead.view",
        "lead.create",
        "lead.update",
        "lead.assign",
        "deal.view",
        "deal.create",
        "deal.update",
        "activity.view",
        "activity.create",
        "activity.update",
        "attachment.view",
        "attachment.create",
        "note.view",
        "note.create",
        "user.view",
    ],
    "Sales Representative": [
        "dashboard.view",
        "company.view",
        "contact.view",
        "contact.create",
        "contact.update",
        "lead.view",
        "lead.create",
        "lead.update",
        "deal.view",
        "deal.create",
        "deal.update",
        "activity.view",
        "activity.create",
        "attachment.view",
        "attachment.create",
        "note.view",
        "note.create",
    ],
    "Support": [
        "dashboard.view",
        "company.view",
        "contact.view",
        "activity.view",
        "activity.create",
        "attachment.view",
        "attachment.create",
        "note.view",
        "note.create",
    ],
    "Marketing": [
        "dashboard.view",
        "company.view",
        "contact.view",
        "lead.view",
        "activity.view",
        "attachment.view",
        "note.view",
    ],
    "Viewer": [
        "dashboard.view",
        "company.view",
        "contact.view",
        "lead.view",
        "deal.view",
        "activity.view",
        "attachment.view",
        "note.view",
    ],
}


def seed_roles(command):

    all_permissions = Permission.objects.all()

    for role_name, permissions in ROLE_PERMISSIONS.items():
        role, _ = Role.objects.update_or_create(
            name=role_name,
        )

        if permissions == "__all__":
            role.permissions.set(all_permissions)
        else:
            role.permissions.set(Permission.objects.filter(code__in=permissions))

    command.stdout.write(command.style.SUCCESS("✓ Roles seeded"))
