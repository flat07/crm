// frontend/src/features/auth/pages/DashboardPage.tsx

import { Button } from "@/components/ui/button";

import { useAuth } from "@/contexts/AuthContext";
import CompaniesPage from "@/features/companies/pages/CompaniesPage";
import { useNavigate } from "react-router-dom";

export default function DashboardPage() {
  const { user } = useAuth();
  const navigate = useNavigate();

  return (
    <main className="p-8">
      <div className="flex flex-col gap-4">
        <div>
          <h1 className="text-3xl font-bold">Dashboard</h1>

          <p>Welcome {user?.email}</p>
        </div>
        <CompaniesPage />

        {/* Container for buttons */}
        <div className="flex flex-wrap gap-4">
          <Button
            variant="outline"
            onClick={() => navigate("/staff/housekeeping")}
          >
            Go to Housekeeping
          </Button>
          <Button
            variant="outline"
            onClick={() => navigate("/staff/engineering")}
          >
            Go to Engineering
          </Button>

          <Button
            variant="outline"
            onClick={() => navigate("/staff/room-service")}
          >
            Go to Room Service
          </Button>
        </div>
      </div>
    </main>
  );
}
