// frontend/src/features/deals/hooks/useDeal.ts
import { useQuery } from "@tanstack/react-query";

import { queryKeys } from "@/lib/queryKeys";

import { getDeal } from "../api/dealsApi";

export function useDeal(id: number) {
  return useQuery({
    queryKey: queryKeys.deals.detail(id),

    queryFn: () => getDeal(id),

    enabled: !!id,
  });
}
