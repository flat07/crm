// frontend/src/routes/RequirePermission.tsx

import { Navigate } from "react-router-dom";

import { usePermissions } from "@/features/auth/hooks/usePermissions";

interface Props {
  permission: string;
  children: React.ReactElement;
}

export default function RequirePermission({ permission, children }: Props) {
  const { can } = usePermissions();

  if (!can(permission)) {
    return <Navigate to="/403" replace />;
  }

  return children;
}
