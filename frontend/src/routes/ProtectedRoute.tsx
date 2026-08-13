// frontend/src/routes/ProtectedRoute.tsx

import { Navigate, Outlet } from "react-router-dom";

import LoadingPage from "@/components/shared/LoadingPage";
import { useAuth } from "@/contexts/AuthContext";

export default function ProtectedRoute() {
  const { loading, isAuthenticated } = useAuth();

  if (loading) {
    return <LoadingPage />;
  }

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  return <Outlet />;
}
