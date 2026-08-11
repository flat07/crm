// frontend/src/features/deals/hooks/useDeals.ts
import { useQuery } from "@tanstack/react-query";

import { queryKeys } from "@/lib/queryKeys";

import { getDeals } from "../api/dealsApi";

interface Props {
  page: number;
  search: string;
  ordering: string;
}

export function useDeals({ page, search, ordering }: Props) {
  return useQuery({
    queryKey: queryKeys.deals.list(page, search, ordering),

    queryFn: () =>
      getDeals({
        page,
        search,
        ordering,
      }),

    placeholderData: (previous) => previous,
  });
}
