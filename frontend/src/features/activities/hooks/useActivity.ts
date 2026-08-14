// frontend/src/features/activities/hooks/useActivity.ts

import { useQuery } from "@tanstack/react-query";

import { getActivity } from "../api/activitiesApi";

export function useActivity(id: string | undefined) {
  return useQuery({
    queryKey: ["activities", id],
    queryFn: () => getActivity(id!),
    enabled: !!id,
  });
}
