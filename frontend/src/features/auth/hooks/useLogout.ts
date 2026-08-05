// frontend/src/features/auth/hooks/useLogout.ts

import { useNavigate } from "react-router-dom";

import { useAuth } from "@/contexts/AuthContext";

export function useLogout() {
  const navigate = useNavigate();

  const { logout } = useAuth();

  return function handleLogout() {
    logout();

    navigate("/login", {
      replace: true,
    });
  };
}
