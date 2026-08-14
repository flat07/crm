// frontend/src/app/staff.tsx

import GuestRoute from "@/routes/GuestRoute";
import ProtectedRoute from "@/routes/ProtectedRoute";
import RequirePermission from "@/routes/RequirePermission";

import ActivitiesPage from "@/features/activities/pages/ActivitiesPage";
import DashboardPage from "@/features/auth/pages/DashboardPage";
import LoginPage from "@/features/auth/pages/LoginPage";
import { PERMISSIONS } from "@/features/auth/utils/permissions";
import CompaniesPage from "@/features/companies/pages/CompaniesPage";
import ContactsPage from "@/features/contacts/pages/ContactsPage";
import DealsPage from "@/features/deals/pages/DealsPage";
import LeadsPage from "@/features/leads/pages/LeadsPage";

import { StaffLayout } from "@/components/layout/staff/StaffLayout";

export const staffRoutes = [
  {
    element: <GuestRoute />,
    children: [
      {
        path: "/login",
        element: <LoginPage />,
      },
    ],
  },
  {
    element: <ProtectedRoute />,
    children: [
      {
        element: <StaffLayout />,
        children: [
          {
            path: "/dashboard",
            element: (
              <RequirePermission permission={PERMISSIONS.DASHBOARD_VIEW}>
                <DashboardPage />
              </RequirePermission>
            ),
          },

          {
            path: "/companies",
            element: (
              <RequirePermission permission={PERMISSIONS.COMPANY_VIEW}>
                <CompaniesPage />
              </RequirePermission>
            ),
          },

          {
            path: "/contacts",
            element: (
              <RequirePermission permission={PERMISSIONS.CONTACT_VIEW}>
                <ContactsPage />
              </RequirePermission>
            ),
          },

          {
            path: "/leads",
            element: (
              <RequirePermission permission={PERMISSIONS.CONTACT_VIEW}>
                <LeadsPage />
              </RequirePermission>
            ),
          },

          {
            path: "/deals",
            element: (
              <RequirePermission permission={PERMISSIONS.DEAL_VIEW}>
                <DealsPage />
              </RequirePermission>
            ),
          },
          {
            path: "/activities",
            element: (
              <RequirePermission permission={PERMISSIONS.DEAL_VIEW}>
                <ActivitiesPage />
              </RequirePermission>
            ),
          },
        ],
      },
    ],
  },
];
