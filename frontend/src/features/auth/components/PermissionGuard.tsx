import { usePermissions } from "../hooks/usePermissions";
interface Props {
  permission: string;
  children: React.ReactNode;
}

export function PermissionGuard({ permission, children }: Props) {
  const { can } = usePermissions();

  if (!can(permission)) {
    return null;
  }

  return <>{children}</>;
}
