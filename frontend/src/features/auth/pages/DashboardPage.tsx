// frontend/src/features/auth/pages/DashboardPage.tsx

import { Button } from "@/components/ui/button";

import { PageContent } from "@/components/layout/staff/PageContent";
import { PageHeader } from "@/components/layout/staff/PageHeader";
import { useAuth } from "@/contexts/AuthContext";
import { useNavigate } from "react-router-dom";

export default function DashboardPage() {
  const { user } = useAuth();
  const navigate = useNavigate();

  return (
    <>
      <PageHeader title="Dashboard" description="Manage your Dashboard" />
      <PageContent>
        <div>
          <p>Welcome {user?.email}</p>
          <div className="flex flex-wrap gap-4">
            <Button variant="outline" onClick={() => navigate("/companies")}>
              Go to Companies
            </Button>
            <Button variant="outline" onClick={() => navigate("/deals")}>
              Go to Deals
            </Button>
            <Button variant="outline" onClick={() => navigate("/contacts")}>
              Go to Contacts
            </Button>
            <Button variant="outline" onClick={() => navigate("/leads")}>
              Go to Leads
            </Button>
            <Button variant="outline" onClick={() => navigate("/activities")}>
              Go to Activities
            </Button>
          </div>
        </div>
      </PageContent>
    </>
  );
}
