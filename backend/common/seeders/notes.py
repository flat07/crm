from companies.models import Company
from contacts.models import Contact
from deals.models import Deal
from django.contrib.contenttypes.models import ContentType
from leads.models import Lead
from notes.models import Note
from staff.models import User

NOTES = [
    {
        "model": Company,
        "lookup": {"name": "CloudNova"},
        "title": "Implementation requirements",
        "content": (
            "CloudNova is interested in migrating their existing CRM "
            "process to our platform. They need reporting, automation, "
            "and role-based access control."
        ),
        "is_pinned": True,
        "is_private": False,
    },
    {
        "model": Company,
        "lookup": {"name": "Bright Education"},
        "title": "Company requirements",
        "content": (
            "Bright Education needs a centralized system for managing "
            "sales contacts, leads, and customer communication."
        ),
        "is_pinned": False,
        "is_private": False,
    },
    {
        "model": Contact,
        "lookup": {"email": "john.smith@acme-tech.com"},
        "title": "Initial conversation",
        "content": (
            "John is interested in learning more about the enterprise "
            "CRM package. Follow up with pricing and implementation details."
        ),
        "is_pinned": True,
        "is_private": False,
    },
    {
        "model": Contact,
        "lookup": {"email": "grace@nextgenai.ai"},
        "title": "Follow-up discussion",
        "content": (
            "Grace requested additional information about integrations "
            "and API capabilities."
        ),
        "is_pinned": False,
        "is_private": False,
    },
    {
        "model": Lead,
        "lookup": {"title": "Enterprise CRM Implementation"},
        "title": "Discovery call notes",
        "content": (
            "The prospect currently uses several disconnected tools. "
            "Main priorities are automation, reporting, and centralized "
            "customer data."
        ),
        "is_pinned": True,
        "is_private": False,
    },
    {
        "model": Lead,
        "lookup": {"title": "Sales Automation Platform"},
        "title": "Qualification notes",
        "content": (
            "The prospect has a sales team of approximately 25 users. "
            "They are looking for lead management and automated follow-ups."
        ),
        "is_pinned": False,
        "is_private": False,
    },
    {
        "model": Deal,
        "lookup": {"lead__title": "Customer Relationship System"},
        "title": "Contract negotiation",
        "content": (
            "Customer requested changes to the implementation timeline "
            "and payment schedule. Legal review is still pending."
        ),
        "is_pinned": True,
        "is_private": False,
    },
    {
        "model": Deal,
        "lookup": {"lead__title": "Hotel Guest Management"},
        "title": "Project kickoff",
        "content": (
            "Kickoff completed successfully. Customer expects the first "
            "working version within the agreed implementation period."
        ),
        "is_pinned": False,
        "is_private": False,
    },
    {
        "model": Deal,
        "lookup": {"lead__title": "Cloud CRM Migration"},
        "title": "Internal pricing discussion",
        "content": (
            "Internal team discussed migration costs, implementation "
            "effort, and possible discount options."
        ),
        "is_pinned": False,
        "is_private": True,
    },
    {
        "model": Deal,
        "lookup": {"lead__title": "AI Sales Platform"},
        "title": "Competitor analysis",
        "content": (
            "The customer is also evaluating two competing CRM platforms. "
            "Our main differentiators are workflow automation and flexible "
            "API integration."
        ),
        "is_pinned": False,
        "is_private": True,
    },
]


def seed_notes(command):
    admin = User.objects.get(
        email="admin@a.com",
    )

    for data in NOTES:
        obj = data["model"].objects.get(
            **data["lookup"],
        )

        content_type = ContentType.objects.get_for_model(
            obj,
        )

        Note.objects.update_or_create(
            content_type=content_type,
            object_id=obj.pk,
            title=data["title"],
            defaults={
                "content": data["content"],
                "created_by": admin,
                "is_pinned": data["is_pinned"],
                "is_private": data["is_private"],
            },
        )

    command.stdout.write(
        command.style.SUCCESS(
            f"✓ Seeded {len(NOTES)} notes",
        )
    )
