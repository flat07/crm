# backend/config/api/urls.py
from django.urls import include, path

urlpatterns = [
    path(
        "companies/",
        include("companies.urls"),
    ),
    path(
        "contacts/",
        include("contacts.urls"),
    ),
    path(
        "deals/",
        include("deals.urls"),
    ),
    path(
        "leads/",
        include("leads.urls"),
    ),
    path(
        "staff/",
        include("staff.urls"),
    ),
]
# /api/v1/companies/
# /api/v1/contacts/
# /api/v1/staff/
