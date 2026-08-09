import { useMutation } from "@tanstack/react-query";

import { deleteCompany } from "../api/companyMutations";

import { queryClient } from "@/lib/query-client";

import { queryKeys } from "@/lib/queryKeys";

export function useDeleteCompany() {
  return useMutation({
    mutationFn: deleteCompany,

    onSuccess() {
      queryClient.invalidateQueries({
        queryKey: queryKeys.companies.all,
      });
    },
  });
}
