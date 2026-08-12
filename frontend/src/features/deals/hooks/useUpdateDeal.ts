// frontend/src/features/deals/hooks/useUpdateDeal.ts

import { getApiErrorMessage } from "@/lib/apiError";
import { queryClient } from "@/lib/query-client";
import { queryKeys } from "@/lib/queryKeys";

import { useMutation } from "@tanstack/react-query";
import { toast } from "sonner";

import { updateDeal } from "../api/dealsMutations";

export function useUpdateDeal() {
  return useMutation({
    mutationFn: ({
      id,
      values,
    }: {
      id: number;
      values: Parameters<typeof updateDeal>[1];
    }) => updateDeal(String(id), values),

    onSuccess: async () => {
      // console.log("✅ UPDATE DEAL SUCCESS");

      await queryClient.invalidateQueries({
        queryKey: queryKeys.deals.all,
      });

      toast.success("Deal updated successfully.");
    },

    onError: (error) => {
      // console.error("🔥 UPDATE DEAL ERROR:", error);

      toast.error("Unable to update deal", {
        description: getApiErrorMessage(error),
      });
    },
  });
}
