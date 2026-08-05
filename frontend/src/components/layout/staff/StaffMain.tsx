// frontend/src/components/layout/staff/StaffMain.tsx

import { Outlet } from "react-router-dom";
import { Footer } from "./Footer";
import { Header } from "./Header";

export function StaffMain() {
  return (
    <div className="flex min-h-screen flex-col bg-muted/20">
      <Header />

      <main className="container mx-auto flex-1 px-4 py-8">
        <Outlet />
      </main>

      <Footer />
    </div>
  );
}
