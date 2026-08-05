// frontend/src/components/shared/NotFound.tsx

import { Link } from "react-router-dom";

import { Button } from "@/components/ui/button";

export default function NotFound() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center gap-6 p-6 text-center">
      <div className="space-y-2">
        <h1 className="text-5xl font-bold">404</h1>

        <p className="text-muted-foreground">Page not found.</p>
      </div>

      <Button asChild>
        <Link to="/">Go Back</Link>
      </Button>
    </div>
  );
}
