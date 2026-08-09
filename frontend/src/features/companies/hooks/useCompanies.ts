// frontend/src/features/companies/hooks/useCompanies.ts
import { useQuery } from "@tanstack/react-query";

import { getCompanies } from "../api/companyApi";

import { queryKeys } from "@/lib/queryKeys";

interface Props {
  page: number;
  search: string;
  ordering: string;
}

export function useCompanies({ page, search, ordering }: Props) {
  return useQuery({
    queryKey: queryKeys.companies.list(page, search),

    queryFn: () =>
      getCompanies({
        page,
        search,
        ordering,
      }),

    placeholderData: (previous) => previous,
  });
}
