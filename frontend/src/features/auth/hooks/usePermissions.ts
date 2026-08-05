// frontend/src/features/auth/hooks/usePermissions.ts
import { useAuth } from "@/contexts/AuthContext";

export function usePermissions() {
  const { user } = useAuth();

  const permissions = user?.permissions ?? [];

  const can = (permission: string) => permissions.includes(permission);

  const canAny = (...perms: string[]) =>
    perms.some((p) => permissions.includes(p));

  const canAll = (...perms: string[]) =>
    perms.every((p) => permissions.includes(p));

  return {
    permissions,
    can,
    canAny,
    canAll,
  };
}
