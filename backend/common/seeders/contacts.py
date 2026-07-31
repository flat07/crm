# contacts/seeders/contacts.py
import random

from companies.models import Company
from contacts.models import Contact
from faker import Faker
from staff.models import User

CONTACTS = [
    {
        "company": "Acme Technologies",
        "first_name": "John",
        "last_name": "Smith",
        "job_title": "Chief Executive Officer",
        "email": "john.smith@acme-tech.com",
        "phone": "+1 555 100 1001",
        "contact_type": "customer",
        "source": "website",
    },
    {
        "company": "Acme Technologies",
        "first_name": "Emily",
        "last_name": "Johnson",
        "job_title": "IT Manager",
        "email": "emily.johnson@acme-tech.com",
        "phone": "+1 555 100 1002",
        "contact_type": "customer",
        "source": "referral",
    },
    {
        "company": "Global Finance Group",
        "first_name": "Michael",
        "last_name": "Brown",
        "job_title": "Finance Director",
        "email": "michael.brown@globalfinance.com",
        "phone": "+44 20 1234 5601",
        "contact_type": "customer",
        "source": "event",
    },
    {
        "company": "Global Finance Group",
        "first_name": "Sarah",
        "last_name": "Wilson",
        "job_title": "Operations Manager",
        "email": "sarah.wilson@globalfinance.com",
        "phone": "+44 20 1234 5602",
        "contact_type": "customer",
        "source": "website",
    },
    {
        "company": "MediCare Solutions",
        "first_name": "David",
        "last_name": "Lee",
        "job_title": "Hospital Administrator",
        "email": "david.lee@medicaresolutions.com",
        "phone": "+1 555 300 2001",
        "contact_type": "customer",
        "source": "referral",
    },
    {
        "company": "Bright Education",
        "first_name": "Sophia",
        "last_name": "Taylor",
        "job_title": "School Director",
        "email": "sophia.taylor@brightedu.com",
        "phone": "+61 2 8000 1001",
        "contact_type": "lead",
        "source": "website",
    },
    {
        "company": "Sunrise Hotels",
        "first_name": "Ahmed",
        "last_name": "Al Mansoori",
        "job_title": "General Manager",
        "email": "ahmed@sunrisehotels.com",
        "phone": "+971 4 555 0102",
        "contact_type": "customer",
        "source": "event",
    },
    {
        "company": "Retail Hub",
        "first_name": "Olivia",
        "last_name": "White",
        "job_title": "Procurement Manager",
        "email": "olivia.white@retailhub.com",
        "phone": "+1 555 800 9001",
        "contact_type": "partner",
        "source": "referral",
    },
    {
        "company": "CloudNova",
        "first_name": "Daniel",
        "last_name": "Walker",
        "job_title": "CTO",
        "email": "daniel.walker@cloudnova.io",
        "phone": "+1 555 222 1112",
        "contact_type": "lead",
        "source": "social_media",
    },
    {
        "company": "NextGen AI",
        "first_name": "Grace",
        "last_name": "Miller",
        "job_title": "Founder",
        "email": "grace@nextgenai.ai",
        "phone": "+1 555 999 8889",
        "contact_type": "lead",
        "source": "cold_call",
    },
]

CONTACT_TYPES = ["customer", "lead", "partner", "vendor", "prospect"]
SOURCES = [
    "website",
    "referral",
    "event",
    "social_media",
    "cold_call",
    "email_campaign",
    "trade_show",
    "linkedin",
]
JOB_TITLES = [
    "Chief Executive Officer",
    "Chief Technology Officer",
    "Chief Financial Officer",
    "VP of Engineering",
    "VP of Sales",
    "IT Manager",
    "Finance Director",
    "Operations Manager",
    "Marketing Manager",
    "Sales Director",
    "Product Manager",
    "Software Engineer",
    "Business Analyst",
    "HR Director",
    "Procurement Manager",
    "General Manager",
    "Founder",
    "Managing Director",
    "Account Executive",
    "Customer Success Manager",
    "Project Manager",
    "Data Scientist",
    "Legal Counsel",
    "Office Administrator",
    "Technical Lead",
]


def seed_contacts(command):
    fake = Faker()
    admin = User.objects.get(email="admin@a.com")
    companies = list(Company.objects.all())
    total_created = 0

    # 1. Seed hardcoded contacts
    for data in CONTACTS:
        company = Company.objects.get(name=data["company"])

        Contact.objects.update_or_create(
            email=data["email"],
            defaults={
                "first_name": data["first_name"],
                "last_name": data["last_name"],
                "job_title": data["job_title"],
                "phone": data["phone"],
                "contact_type": data["contact_type"],
                "source": data["source"],
                "company": company,
                "owner": admin,
                "city": company.city,
                "country": company.country,
            },
        )
        total_created += 1

    # 2. Seed 20–50 Faker-generated contacts
    faker_count = random.randint(20, 50)

    for _ in range(faker_count):
        company = random.choice(companies)
        first_name = fake.first_name()
        last_name = fake.last_name()
        job_title = random.choice(JOB_TITLES)
        contact_type = random.choice(CONTACT_TYPES)
        source = random.choice(SOURCES)

        # Generate a realistic email
        domain = fake.domain_name()
        email_formats = [
            f"{first_name.lower()}.{last_name.lower()}@{domain}",
            f"{first_name.lower()[0]}{last_name.lower()}@{domain}",
            f"{first_name.lower()}@{domain}",
            f"{last_name.lower()}.{first_name.lower()}@{domain}",
        ]
        email = random.choice(email_formats)

        # Generate a phone number (international format if company has country info)
        if company.country and company.country.lower() in [
            "united kingdom",
            "uk",
            "gb",
        ]:
            phone = fake.numerify("+44 7## ### ####")
        elif company.country and company.country.lower() in [
            "united states",
            "usa",
            "us",
        ]:
            phone = fake.numerify("+1 ### ### ####")
        elif company.country and company.country.lower() in ["australia", "au"]:
            phone = fake.numerify("+61 4## ### ###")
        else:
            phone = fake.phone_number()

        Contact.objects.update_or_create(
            email=email,
            defaults={
                "first_name": first_name,
                "last_name": last_name,
                "job_title": job_title,
                "phone": phone,
                "contact_type": contact_type,
                "source": source,
                "company": company,
                "owner": admin,
                "city": company.city,
                "country": company.country,
            },
        )
        total_created += 1

    command.stdout.write(
        command.style.SUCCESS(
            f"✓ Seeded {len(CONTACTS)} hardcoded + {faker_count} Faker contacts = {total_created} total contacts"
        )
    )
