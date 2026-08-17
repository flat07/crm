// frontend/src/features/activities/api/activitiesApi.ts
import { api } from "@/lib/axios";

import type { PaginatedResponse } from "@/types/pagination";
import type { Activity, ActivityFormData, ActivityQueryParams } from "../types";
/**
 * Get activities
 */
export async function getActivities(
  params: ActivityQueryParams,
): Promise<PaginatedResponse<Activity>> {
  const { data } = await api.get<PaginatedResponse<Activity>>("/activities/", {
    params,
  });
  // console.log("DEBUG: getActivities: data ", data);

  return data;
}

/**
 * Get a single activity
 */
export async function getActivity(id: string): Promise<Activity> {
  const { data } = await api.get<Activity>(`/activities/${id}/`);

  return data;
}

/**
 * Create an activity
 */
export async function createActivity(
  values: ActivityFormData,
): Promise<Activity> {
  const { data } = await api.post<Activity>("/activities/", values);

  return data;
}

/**
 * Update an activity
 */
export async function updateActivity(
  id: string,
  values: Partial<ActivityFormData>,
): Promise<Activity> {
  const { data } = await api.patch<Activity>(`/activities/${id}/`, values);
  // console.log("DEBUG: updateActivity: data ", data);
  return data;
}

/**
 * Delete an activity
 */
export async function deleteActivity(id: string): Promise<void> {
  await api.delete(`/activities/${id}/`);
}
