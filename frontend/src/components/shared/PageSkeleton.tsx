// frontend/src/components/shared/PageSkeleton.tsx

import { Skeleton } from "@/components/ui/skeleton";

export default function PageSkeleton() {
  return (
    <div className="space-y-4 p-6">
      <Skeleton className="h-10 w-44" />

      <Skeleton className="h-28 rounded-xl" />

      <Skeleton className="h-24 rounded-xl" />

      <Skeleton className="h-24 rounded-xl" />

      <Skeleton className="h-24 rounded-xl" />
    </div>
  );
}
