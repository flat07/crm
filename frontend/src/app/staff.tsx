// src/routes/staff.tsx

import GuestRoute from "@/routes/GuestRoute";
import ProtectedRoute from "@/routes/ProtectedRoute";

import DashboardPage from "@/features/auth/pages/DashboardPage";
import LoginPage from "@/features/auth/pages/LoginPage";

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
        element: <DashboardPage />,
      },
    ],
  },
];
