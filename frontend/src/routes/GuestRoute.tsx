// frontend/src/routes/GuestRoute.tsx

import { Navigate, Outlet } from "react-router-dom";

import LoadingPage from "@/components/shared/LoadingPage";
import { useAuth } from "@/contexts/AuthContext";

export default function GuestRoute() {
  const { loading, isAuthenticated } = useAuth();

  if (loading) {
    return <LoadingPage />;
  }

  if (isAuthenticated) {
    return <Navigate to="/dashboard" replace />;
  }

  return <Outlet />;
}
