# backend/common/seeders/staff.py

from common.seeders.departments import seed_departments
from common.seeders.permissions import seed_permissions
from common.seeders.roles import seed_roles
from common.seeders.users import seed_users


def seed_staff(command):
    seed_departments(command)
    seed_permissions(command)
    seed_roles(command)
    seed_users(command)
