// frontend/src/features/deals/hooks/useCreateDeal.ts
import { queryClient } from "@/lib/query-client";
import { queryKeys } from "@/lib/queryKeys";
import { useMutation } from "@tanstack/react-query";
import { toast } from "sonner";

import { getApiErrorMessage } from "@/lib/apiError";
import { createDeal } from "../api/dealsMutations";

export function useCreateDeal() {
  console.log("🔥 createDeal CALLED");
  return useMutation({
    mutationFn: createDeal,

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: queryKeys.deals.all,
      });
      console.log("✅ createDeal SUCCESS:");
      toast.success("Deal created successfully.");
    },

    onError: (error) => {
      console.log("🔥 MUTATION ERROR:", error);

      toast.error("Unable to create deal", {
        description: getApiErrorMessage(error),
      });
    },
  });
}
