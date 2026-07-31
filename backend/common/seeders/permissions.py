# staff/seeders/permissions.py

from staff.models import Permission

PERMISSIONS = [
    ("company.view", "View Companies"),
    ("company.create", "Create Companies"),
    ("company.update", "Update Companies"),
    ("company.delete", "Delete Companies"),
    ("contact.view", "View Contacts"),
    ("contact.create", "Create Contacts"),
    ("contact.update", "Update Contacts"),
    ("contact.delete", "Delete Contacts"),
    ("lead.view", "View Leads"),
    ("lead.create", "Create Leads"),
    ("lead.update", "Update Leads"),
    ("lead.delete", "Delete Leads"),
    ("lead.assign", "Assign Leads"),
    ("deal.view", "View Deals"),
    ("deal.create", "Create Deals"),
    ("deal.update", "Update Deals"),
    ("deal.delete", "Delete Deals"),
    ("activity.view", "View Activities"),
    ("activity.create", "Create Activities"),
    ("activity.update", "Update Activities"),
    ("activity.delete", "Delete Activities"),
    ("attachment.view", "View Attachments"),
    ("attachment.create", "Create Attachments"),
    ("attachment.delete", "Delete Attachments"),
    ("note.view", "View Notes"),
    ("note.create", "Create Notes"),
    ("note.delete", "Delete Notes"),
    ("user.view", "View Users"),
    ("user.create", "Create Users"),
    ("user.update", "Update Users"),
    ("user.delete", "Delete Users"),
    ("dashboard.view", "View Dashboard"),
]


def seed_permissions(command):

    for code, name in PERMISSIONS:
        Permission.objects.update_or_create(
            code=code,
            defaults={
                "name": name,
            },
        )

    command.stdout.write(command.style.SUCCESS("✓ Permissions seeded"))
