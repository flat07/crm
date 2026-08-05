// frontend/src/components/layout/staff/Header.tsx

import { Button } from "@/components/ui/button";
import { useLogout } from "@/features/auth/hooks/useLogout";
import { Link } from "react-router-dom";
import AppLogo from "../AppLogo";

export function Header() {
  const handleLogout = useLogout();
  return (
    <header className="border-b bg-background">
      <div className="container mx-auto flex h-16 items-center justify-between px-4">
        <Link to="/dashboard" className="flex items-center gap-2">
          <AppLogo />
        </Link>

        <div className="rounded-lg border px-4 py-2">
          <p className="text-xs text-muted-foreground">Me</p>
        </div>
        <Button variant="destructive" onClick={handleLogout}>
          Logout
        </Button>
      </div>
    </header>
  );
}
