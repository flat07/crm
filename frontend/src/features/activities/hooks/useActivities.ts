// frontend/src/features/activities/hooks/useActivities.ts

import { useQuery } from "@tanstack/react-query";

import { GridQueryParams } from "@/components/shared/DataGrid";

import { getActivities } from "../api/activitiesApi";

export function useActivities(params: GridQueryParams) {
  return useQuery({
    queryKey: ["activities", params],
    queryFn: () => getActivities(params),
  });
}
