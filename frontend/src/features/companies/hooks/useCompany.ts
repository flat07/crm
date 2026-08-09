import { useQuery } from "@tanstack/react-query";

import { getCompany } from "../api/companyApi";

import { queryKeys } from "@/lib/queryKeys";

export function useCompany(id: number) {
  return useQuery({
    queryKey: queryKeys.companies.detail(id),

    queryFn: () => getCompany(id),

    enabled: !!id,
  });
}
