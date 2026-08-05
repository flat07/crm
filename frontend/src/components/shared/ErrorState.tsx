// frontend/src/components/shared/ErrorState.tsx

import { Button } from "@/components/ui/button";

interface Props {
  title?: string;
  description?: string;
  onRetry?: () => void;
}

export default function ErrorState({
  title = "Something went wrong",
  description = "Please try again.",
  onRetry,
}: Props) {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center gap-4 p-6 text-center">
      <div>
        <h2 className="text-xl font-semibold">{title}</h2>

        <p className="text-muted-foreground">{description}</p>
      </div>

      {onRetry && <Button onClick={onRetry}>Retry</Button>}
    </div>
  );
}
