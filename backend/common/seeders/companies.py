# companies/seeders/companies.py

from companies.models import Company
from staff.models import User

COMPANIES = [
    {
        "name": "Acme Technologies",
        "legal_name": "Acme Technologies LLC",
        "website": "https://acme-tech.com",
        "email": "info@acme-tech.com",
        "phone": "+1 555 100 1000",
        "industry": "technology",
        "company_type": "customer",
        "size": "enterprise",
        "city": "New York",
        "country": "USA",
    },
    {
        "name": "Global Finance Group",
        "legal_name": "Global Finance Group Ltd.",
        "website": "https://globalfinance.com",
        "email": "contact@globalfinance.com",
        "phone": "+44 20 1234 5678",
        "industry": "finance",
        "company_type": "customer",
        "size": "large",
        "city": "London",
        "country": "United Kingdom",
    },
    {
        "name": "MediCare Solutions",
        "legal_name": "MediCare Solutions Inc.",
        "website": "https://medicaresolutions.com",
        "email": "hello@medicaresolutions.com",
        "phone": "+1 555 300 2000",
        "industry": "healthcare",
        "company_type": "customer",
        "size": "large",
        "city": "Chicago",
        "country": "USA",
    },
    {
        "name": "Bright Education",
        "legal_name": "Bright Education Ltd.",
        "website": "https://brightedu.com",
        "email": "info@brightedu.com",
        "phone": "+61 2 8000 1000",
        "industry": "education",
        "company_type": "prospect",
        "size": "medium",
        "city": "Sydney",
        "country": "Australia",
    },
    {
        "name": "Sunrise Hotels",
        "legal_name": "Sunrise Hotels Group",
        "website": "https://sunrisehotels.com",
        "email": "sales@sunrisehotels.com",
        "phone": "+971 4 555 0101",
        "industry": "hospitality",
        "company_type": "customer",
        "size": "enterprise",
        "city": "Dubai",
        "country": "UAE",
    },
    {
        "name": "Retail Hub",
        "legal_name": "Retail Hub LLC",
        "website": "https://retailhub.com",
        "email": "support@retailhub.com",
        "phone": "+1 555 800 9000",
        "industry": "retail",
        "company_type": "partner",
        "size": "large",
        "city": "Los Angeles",
        "country": "USA",
    },
    {
        "name": "CloudNova",
        "legal_name": "CloudNova Inc.",
        "website": "https://cloudnova.io",
        "email": "hello@cloudnova.io",
        "phone": "+1 555 222 1111",
        "industry": "technology",
        "company_type": "prospect",
        "size": "medium",
        "city": "San Francisco",
        "country": "USA",
    },
    {
        "name": "Blue Ocean Logistics",
        "legal_name": "Blue Ocean Logistics Ltd.",
        "website": "https://blueoceanlogistics.com",
        "email": "office@blueoceanlogistics.com",
        "phone": "+65 6123 4567",
        "industry": "other",
        "company_type": "vendor",
        "size": "large",
        "city": "Singapore",
        "country": "Singapore",
    },
    {
        "name": "Green Energy Corp",
        "legal_name": "Green Energy Corporation",
        "website": "https://greenenergy.com",
        "email": "contact@greenenergy.com",
        "phone": "+49 30 123456",
        "industry": "other",
        "company_type": "partner",
        "size": "enterprise",
        "city": "Berlin",
        "country": "Germany",
    },
    {
        "name": "NextGen AI",
        "legal_name": "NextGen AI Ltd.",
        "website": "https://nextgenai.ai",
        "email": "info@nextgenai.ai",
        "phone": "+1 555 999 8888",
        "industry": "technology",
        "company_type": "prospect",
        "size": "small",
        "city": "Austin",
        "country": "USA",
    },
]


def seed_companies(command):
    admin = User.objects.get(email="admin@a.com")

    for company in COMPANIES:
        Company.objects.update_or_create(
            name=company["name"],
            defaults={
                **company,
                "owner": admin,
                "created_by": admin,
            },
        )

    command.stdout.write(command.style.SUCCESS(f"✓ Seeded {len(COMPANIES)} companies"))
