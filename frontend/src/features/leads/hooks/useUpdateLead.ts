// frontend/src/features/leads/hooks/useUpdateLead.ts
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { toast } from "sonner";

import { getApiErrorMessage } from "@/lib/apiError";

import { updateLead, type UpdateLeadData } from "../api/leadsApi";

interface UpdateLeadVariables {
  id: string;
  data: UpdateLeadData;
}

export function useUpdateLead() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ id, data }: UpdateLeadVariables) => updateLead(id, data),

    onSuccess: (updatedLead) => {
      queryClient.invalidateQueries({
        queryKey: ["leads"],
      });

      queryClient.invalidateQueries({
        queryKey: ["leads", updatedLead.id],
      });

      toast.success("Lead updated successfully.");
    },

    onError: (error) => {
      toast.error(getApiErrorMessage(error));
    },
  });
}
