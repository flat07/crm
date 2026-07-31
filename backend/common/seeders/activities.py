from datetime import timedelta

from activities.models import Activity
from companies.models import Company
from contacts.models import Contact
from deals.models import Deal
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from leads.models import Lead
from staff.models import User

ACTIVITIES = [
    {
        "model": Lead,
        "lookup": {"title": "Enterprise CRM Implementation"},
        "title": "Initial discovery call",
        "activity_type": "call",
        "status": "completed",
        "priority": "high",
        "days": -5,
    },
    {
        "model": Lead,
        "lookup": {"title": "Sales Automation Platform"},
        "title": "Qualification call",
        "activity_type": "call",
        "status": "completed",
        "priority": "medium",
        "days": -2,
    },
    {
        "model": Contact,
        "lookup": {"email": "john.smith@acme-tech.com"},
        "title": "Send product brochure",
        "activity_type": "email",
        "status": "completed",
        "priority": "medium",
        "days": -1,
    },
    {
        "model": Contact,
        "lookup": {"email": "grace@nextgenai.ai"},
        "title": "Follow-up email",
        "activity_type": "email",
        "status": "planned",
        "priority": "high",
        "days": 2,
    },
    {
        "model": Deal,
        "lookup": {"lead__title": "Customer Relationship System"},
        "title": "Contract negotiation meeting",
        "activity_type": "meeting",
        "status": "planned",
        "priority": "urgent",
        "days": 3,
    },
    {
        "model": Deal,
        "lookup": {"lead__title": "Hotel Guest Management"},
        "title": "Project kickoff meeting",
        "activity_type": "meeting",
        "status": "completed",
        "priority": "high",
        "days": -3,
    },
    {
        "model": Company,
        "lookup": {"name": "CloudNova"},
        "title": "Prepare implementation proposal",
        "activity_type": "task",
        "status": "in_progress",
        "priority": "high",
        "days": 4,
    },
    {
        "model": Company,
        "lookup": {"name": "Bright Education"},
        "title": "Verify company requirements",
        "activity_type": "task",
        "status": "planned",
        "priority": "medium",
        "days": 5,
    },
    {
        "model": Deal,
        "lookup": {"lead__title": "Cloud CRM Migration"},
        "title": "Internal pricing notes",
        "activity_type": "note",
        "status": "completed",
        "priority": "low",
        "days": -1,
    },
    {
        "model": Deal,
        "lookup": {"lead__title": "AI Sales Platform"},
        "title": "Competitor analysis",
        "activity_type": "note",
        "status": "completed",
        "priority": "medium",
        "days": -2,
    },
]


def seed_activities(command):

    admin = User.objects.get(email="admin@a.com")

    for data in ACTIVITIES:
        obj = data["model"].objects.get(**data["lookup"])

        content_type = ContentType.objects.get_for_model(obj)

        due = timezone.now() + timedelta(days=data["days"])

        completed = due if data["status"] == "completed" else None

        Activity.objects.update_or_create(
            title=data["title"],
            content_type=content_type,
            object_id=obj.pk,
            defaults={
                "description": f"{data['title']} for {obj}",
                "activity_type": data["activity_type"],
                "status": data["status"],
                "priority": data["priority"],
                "due_date": due,
                "completed_at": completed,
                "owner": admin,
                "created_by": admin,
            },
        )

    command.stdout.write(
        command.style.SUCCESS(f"✓ Seeded {len(ACTIVITIES)} activities")
    )
