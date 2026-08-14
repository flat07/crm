// frontend/src/features/activities/hooks/useDeleteActivity.ts

import { useMutation, useQueryClient } from "@tanstack/react-query";

import { deleteActivity } from "../api/activitiesApi";

export function useDeleteActivity() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (id: string) => deleteActivity(id),

    onSuccess: (_, id) => {
      queryClient.removeQueries({
        queryKey: ["activities", id],
      });

      queryClient.invalidateQueries({
        queryKey: ["activities"],
      });
    },
  });
}
