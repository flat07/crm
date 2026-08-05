// frontend/src/components/shared/SubmitButton.tsx

import { Loader2 } from "lucide-react";

import { Button } from "@/components/ui/button";

interface Props {
  isPending: boolean;
  children: React.ReactNode;
}

export default function SubmitButton({ isPending, children }: Props) {
  return (
    <Button type="submit" className="w-full" disabled={isPending}>
      {isPending && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}

      {children}
    </Button>
  );
}
