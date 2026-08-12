// frontend/src/features/leads/hooks/useDeleteLead.ts
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { toast } from "sonner";

import { getApiErrorMessage } from "@/lib/apiError";

import { deleteLead } from "../api/leadsApi";

export function useDeleteLead() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (id: string) => deleteLead(id),

    onSuccess: (_, deletedId) => {
      queryClient.invalidateQueries({
        queryKey: ["leads"],
      });

      queryClient.removeQueries({
        queryKey: ["leads", deletedId],
      });

      toast.success("Lead archived successfully.");
    },

    onError: (error) => {
      toast.error(getApiErrorMessage(error));
    },
  });
}
