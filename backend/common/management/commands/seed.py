# backend/common/management/commands/seed.py
from django.core.management.base import BaseCommand

from common.seeders.activities import seed_activities
from common.seeders.companies import seed_companies
from common.seeders.contacts import seed_contacts
from common.seeders.deals import seed_deals
from common.seeders.leads import seed_leads
from common.seeders.staff import seed_staff


class Command(BaseCommand):
    help = "Seed the database"

    def handle(self, *args, **options):
        seeders = [
            seed_staff,
            seed_companies,
            seed_contacts,
            seed_leads,
            seed_deals,
            seed_activities,
        ]

        for seeder in seeders:
            seeder(self)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully."))
