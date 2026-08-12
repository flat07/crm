// src/routes/staff.tsx

import GuestRoute from "@/routes/GuestRoute";
import ProtectedRoute from "@/routes/ProtectedRoute";
import RequirePermission from "@/routes/RequirePermission";

import DashboardPage from "@/features/auth/pages/DashboardPage";
import LoginPage from "@/features/auth/pages/LoginPage";
import { PERMISSIONS } from "@/features/auth/utils/permissions";
import CompaniesPage from "@/features/companies/pages/CompaniesPage";
import ContactsPage from "@/features/contacts/pages/ContactsPage";
import DealsPage from "@/features/deals/pages/DealsPage";
import LeadsPage from "@/features/leads/pages/LeadsPage";

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
        path: "/deals",
        element: (
          <RequirePermission permission={PERMISSIONS.DEAL_VIEW}>
            <DealsPage />
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
    ],
  },
];
