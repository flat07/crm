// frontend/src/features/activities/hooks/useUpdateActivity.ts

import { useMutation, useQueryClient } from "@tanstack/react-query";

import { updateActivity } from "../api/activitiesApi";

import type { ActivityFormData } from "../types";

interface UpdateActivityVariables {
  id: string;
  values: Partial<ActivityFormData>;
}

export function useUpdateActivity() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ id, values }: UpdateActivityVariables) =>
      updateActivity(id, values),

    onSuccess: (activity) => {
      queryClient.invalidateQueries({
        queryKey: ["activities"],
      });

      queryClient.setQueryData(["activities", activity.id], activity);
    },
  });
}
