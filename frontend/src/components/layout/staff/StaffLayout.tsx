// frontend/src/components/layout/staff/StaffLayout.tsx

import { Outlet } from "react-router-dom";

import { Footer } from "./Footer";
import { Header } from "./Header";
import { Sidebar } from "./Sidebar/Sidebar";

export function StaffLayout() {
  return (
    <div className="flex min-h-screen w-full flex-col bg-background">
      {/* Header */}
      <Header />

      {/* Body */}
      <div className="flex min-w-0 flex-1">
        {/* Sidebar */}
        <Sidebar />

        {/* Main */}
        <main className="flex min-w-0 flex-1 flex-col">
          <Outlet />
        </main>
      </div>

      {/* Footer */}
      <Footer />
    </div>
  );
}
