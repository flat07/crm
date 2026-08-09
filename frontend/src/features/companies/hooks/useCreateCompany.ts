import { useMutation } from "@tanstack/react-query";

import { queryClient } from "@/lib/query-client";

import { createCompany } from "../api/companyMutations";

import { queryKeys } from "@/lib/queryKeys";

export function useCreateCompany() {
  return useMutation({
    mutationFn: createCompany,

    onSuccess() {
      queryClient.invalidateQueries({
        queryKey: queryKeys.companies.all,
      });
    },
  });
}
