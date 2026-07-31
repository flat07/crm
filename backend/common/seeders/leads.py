from datetime import timedelta
from decimal import Decimal

from companies.models import Company
from contacts.models import Contact
from django.utils import timezone
from leads.models import Lead, LeadAssignment, LeadStatusHistory
from staff.models import User

LEADS = [
    {
        "company": "Acme Technologies",
        "contact": "John Smith",
        "title": "Enterprise CRM Implementation",
        "status": "qualified",
        "source": "website",
        "estimated_value": Decimal("25000.00"),
        "probability": 60,
        "days": 30,
    },
    {
        "company": "Global Finance Group",
        "contact": "Michael Brown",
        "title": "Sales Automation Platform",
        "status": "proposal_sent",
        "source": "referral",
        "estimated_value": Decimal("48000.00"),
        "probability": 75,
        "days": 14,
    },
    {
        "company": "MediCare Solutions",
        "contact": "David Lee",
        "title": "Customer Relationship System",
        "status": "negotiation",
        "source": "event",
        "estimated_value": Decimal("92000.00"),
        "probability": 90,
        "days": 10,
    },
    {
        "company": "Bright Education",
        "contact": "Sophia Taylor",
        "title": "Student CRM Platform",
        "status": "new",
        "source": "website",
        "estimated_value": Decimal("12000.00"),
        "probability": 20,
        "days": 60,
    },
    {
        "company": "Sunrise Hotels",
        "contact": "Ahmed Al Mansoori",
        "title": "Hotel Guest Management",
        "status": "won",
        "source": "referral",
        "estimated_value": Decimal("68000.00"),
        "probability": 100,
        "days": 0,
    },
    {
        "company": "Retail Hub",
        "contact": "Olivia White",
        "title": "Retail CRM Upgrade",
        "status": "contacted",
        "source": "cold_call",
        "estimated_value": Decimal("18000.00"),
        "probability": 35,
        "days": 45,
    },
    {
        "company": "CloudNova",
        "contact": "Daniel Walker",
        "title": "Cloud CRM Migration",
        "status": "proposal_sent",
        "source": "social_media",
        "estimated_value": Decimal("37000.00"),
        "probability": 70,
        "days": 20,
    },
    {
        "company": "Blue Ocean Logistics",
        "contact": None,
        "title": "Logistics Management Platform",
        "status": "new",
        "source": "email",
        "estimated_value": Decimal("42000.00"),
        "probability": 15,
        "days": 50,
    },
    {
        "company": "Green Energy Corp",
        "contact": None,
        "title": "Renewable Energy CRM",
        "status": "lost",
        "source": "event",
        "estimated_value": Decimal("83000.00"),
        "probability": 0,
        "days": 0,
    },
    {
        "company": "NextGen AI",
        "contact": "Grace Miller",
        "title": "AI Sales Platform",
        "status": "qualified",
        "source": "website",
        "estimated_value": Decimal("56000.00"),
        "probability": 55,
        "days": 25,
    },
]


def seed_leads(command):
    admin = User.objects.get(email="admin@a.com")

    for data in LEADS:
        company = Company.objects.get(name=data["company"])

        contact = None
        if data["contact"]:
            first_name, last_name = data["contact"].split(" ", 1)
            contact = Contact.objects.get(
                company=company,
                first_name=first_name,
                last_name=last_name,
            )

        lead, _ = Lead.objects.update_or_create(
            title=data["title"],
            company=company,
            defaults={
                "contact": contact,
                "source": data["source"],
                "status": data["status"],
                "estimated_value": data["estimated_value"],
                "probability": data["probability"],
                "expected_close_date": (
                    timezone.now() + timedelta(days=data["days"])
                    if data["days"] > 0
                    else None
                ),
                "owner": admin,
                "description": f"{data['title']} opportunity for {company.name}.",
            },
        )

        # ── LeadAssignment (idempotent) ──
        LeadAssignment.objects.update_or_create(
            lead=lead,
            assigned_to=admin,
            defaults={
                "assigned_by": admin,
                "is_active": True,
            },
        )

        # ── LeadStatusHistory (initial transition: new → current) ──
        LeadStatusHistory.objects.get_or_create(
            lead=lead,
            old_status="new",
            new_status=lead.status,
            changed_by=admin,
            defaults={
                "notes": f"Lead moved to {lead.get_status_display()}",  # type: ignore
            },
        )

    command.stdout.write(
        command.style.SUCCESS(f"✓ Seeded {len(LEADS)} leads with assignments & history")
    )
