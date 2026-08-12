// frontend/src/features/leads/hooks/useCreateLead.ts
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { toast } from "sonner";

import { getApiErrorMessage } from "@/lib/apiError";

import { createLead, type CreateLeadData } from "../api/leadsApi";

export function useCreateLead() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (data: CreateLeadData) => createLead(data),

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["leads"],
      });

      toast.success("Lead created successfully.");
    },

    onError: (error) => {
      toast.error(getApiErrorMessage(error));
    },
  });
}
