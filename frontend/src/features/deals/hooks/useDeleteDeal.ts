// frontend/src/features/deals/hooks/useDeleteDeal.ts

import { getApiErrorMessage } from "@/lib/apiError";
import { queryClient } from "@/lib/query-client";
import { queryKeys } from "@/lib/queryKeys";

import { useMutation } from "@tanstack/react-query";
import { toast } from "sonner";

import { deleteDeal } from "../api/dealsMutations";

export function useDeleteDeal() {
  return useMutation({
    mutationFn: deleteDeal,

    onSuccess: async () => {
      // console.log("✅ DELETE DEAL SUCCESS");

      await queryClient.invalidateQueries({
        queryKey: queryKeys.deals.all,
      });

      toast.success("Deal deleted successfully.");
    },

    onError: (error) => {
      // console.error("🔥 DELETE DEAL ERROR:", error);

      toast.error("Unable to delete deal", {
        description: getApiErrorMessage(error),
      });
    },
  });
}
