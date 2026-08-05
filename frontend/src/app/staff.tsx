// src/routes/staff.tsx

import GuestRoute from "@/routes/GuestRoute";
import ProtectedRoute from "@/routes/ProtectedRoute";
import RequirePermission from "@/routes/RequirePermission";

import DashboardPage from "@/features/auth/pages/DashboardPage";
import LoginPage from "@/features/auth/pages/LoginPage";
import { PERMISSIONS } from "@/features/auth/utils/permissions";

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
    ],
  },
];
