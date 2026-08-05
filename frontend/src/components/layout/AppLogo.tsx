// frontend/src/components/layout/AppLogo.tsx

import { Hotel } from "lucide-react";

export default function AppLogo() {
  return (
    <div className="flex items-center gap-3">
      <div className="rounded-xl bg-primary p-3 text-primary-foreground">
        <Hotel className="h-4 w-4" />
      </div>

      <div>
        <h3 className="text-md font-bold">CRM</h3>

        <p className="text-xs text-muted-foreground">Home</p>
      </div>
    </div>
  );
}
