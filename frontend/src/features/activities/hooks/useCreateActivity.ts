// frontend/src/features/activities/hooks/useCreateActivity.ts

import { useMutation, useQueryClient } from "@tanstack/react-query";

import { createActivity } from "../api/activitiesApi";

import type { ActivityFormData } from "../types";

export function useCreateActivity() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (values: ActivityFormData) => createActivity(values),

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["activities"],
      });
    },
  });
}
