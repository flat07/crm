// frontend/src/features/activities/hooks/useActivities.ts

import { useQuery } from "@tanstack/react-query";

import { getActivities } from "../api/activitiesApi";
import type { ActivityQueryParams } from "../types";

export function useActivities(params: ActivityQueryParams) {
  return useQuery({
    queryKey: ["activities", params],
    queryFn: () => getActivities(params),
  });
}
