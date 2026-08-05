// frontend/src/components/layout/PublicLayout.tsx

import { Link, Outlet } from "react-router-dom";

import { Button } from "@/components/ui/button";

import AppLogo from "./AppLogo";
import PublicFooter from "./PublicFooter";

import ThemeToggle from "@/components/shared/ThemeToggle";

export default function PublicLayout() {
  return (
    <div className="min-h-screen bg-muted/30">
      <div className="mx-auto flex min-h-screen max-w-md flex-col">
        <header className="flex items-center justify-between border-b bg-background px-5 py-4">
          <AppLogo />
          <div className="flex items-center gap-2">
            <ThemeToggle />

            <Button size="sm" asChild>
              <Link to="/login">Login</Link>
            </Button>
          </div>
        </header>

        <div className="flex-1">
          <Outlet />
        </div>

        <PublicFooter />
      </div>
    </div>
  );
}
