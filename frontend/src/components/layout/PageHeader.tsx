// frontend/src/components/layout/PageHeader.tsx

import { ChevronLeft } from "lucide-react";
import { useNavigate } from "react-router-dom";

import { Button } from "@/components/ui/button";

interface Props {
  title: string;
  description?: string;
}

export default function PageHeader({ title, description }: Props) {
  const navigate = useNavigate();

  return (
    <header className="sticky top-0 z-50 border-b bg-background">
      <div className="flex items-center gap-3 p-4">
        <Button variant="ghost" size="icon" onClick={() => navigate(-1)}>
          <ChevronLeft className="h-5 w-5" />
        </Button>

        <div>
          <h1 className="text-xl font-semibold">{title}</h1>

          {description && (
            <p className="text-sm text-muted-foreground">{description}</p>
          )}
        </div>
      </div>
    </header>
  );
}
