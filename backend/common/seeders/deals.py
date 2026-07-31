from decimal import Decimal

from deals.models import (
    Deal,
    DealCompetitor,
    DealProduct,
    DealStageHistory,
)
from django.utils import timezone
from leads.models import Lead
from staff.models import User

LEADS_TO_DEALS = {
    "Enterprise CRM Implementation": "proposal",
    "Sales Automation Platform": "proposal",
    "Customer Relationship System": "negotiation",
    "Hotel Guest Management": "won",
    "Cloud CRM Migration": "proposal",
    "AI Sales Platform": "discovery",
}


def seed_deals(command):

    admin = User.objects.get(email="admin@a.com")

    for lead_title, stage in LEADS_TO_DEALS.items():
        lead = Lead.objects.get(title=lead_title)

        deal, _ = Deal.objects.update_or_create(
            lead=lead,
            defaults={
                "company": lead.company,
                "contact": lead.contact,
                "owner": admin,
                "stage": stage,
                "amount": lead.estimated_value,
                "probability": lead.probability,
                "expected_close_date": lead.expected_close_date,
                "actual_close_date": (timezone.now() if stage == "won" else None),
                "description": lead.description,
            },
        )

        DealStageHistory.objects.get_or_create(
            deal=deal,
            old_stage="prospecting",
            new_stage=stage,
            changed_by=admin,
            defaults={
                "notes": f"Moved to {deal.get_stage_display()}",  # type: ignore
            },
        )

        seed_products(deal)
        seed_competitors(deal)

    command.stdout.write(command.style.SUCCESS(f"✓ Seeded {len(LEADS_TO_DEALS)} deals"))


PRODUCTS = [
    ("CRM Enterprise License", 50, Decimal("120.00")),
    ("Implementation Service", 1, Decimal("8500.00")),
    ("Training Package", 5, Decimal("500.00")),
]


def seed_products(deal):

    deal.products.all().delete()

    for name, qty, price in PRODUCTS:
        DealProduct.objects.create(
            deal=deal,
            name=name,
            quantity=qty,
            unit_price=price,
        )


COMPETITORS = [
    "Salesforce",
    "HubSpot",
]


def seed_competitors(deal):

    deal.competitors.all().delete()

    for competitor in COMPETITORS:
        DealCompetitor.objects.create(
            deal=deal,
            name=competitor,
            notes="Common competitor in enterprise CRM market.",
        )
