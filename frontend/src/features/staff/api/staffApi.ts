// frontend/src/features/staff/api/staffApi.ts
import { api } from "@/lib/axios";
import type { PaginatedResponse } from "@/types/api";
import type {
  CreateStaffData,
  StaffListParams,
  StaffUserDetail,
  StaffUserList,
} from "../types";

export type UpdateStaffData = Partial<Omit<CreateStaffData, "password">>;

/**
 * Get paginated list of staff users with optional filters
 */
export async function getStaff(params: StaffListParams = {}) {
  const { data } = await api.get<PaginatedResponse<StaffUserList>>(
    "/auth/users/",
    {
      params,
    },
  );
  return data;
}

/**
 * Get a single staff user by ID with full details
 */
export async function getStaffUser(id: number | string) {
  const { data } = await api.get<StaffUserDetail>(`/auth/users/${id}/`);
  return data;
}

/**
 * Create a new staff user
 */
export async function createStaffUser(staffData: CreateStaffData) {
  const { data } = await api.post<StaffUserDetail>("/auth/users/", staffData);
  return data;
}

/**
 * Update an existing staff user
 */
export async function updateStaffUser(
  id: number | string,
  staffData: UpdateStaffData,
) {
  const { data } = await api.patch<StaffUserDetail>(
    `/auth/users/${id}/`,
    staffData,
  );
  return data;
}

/**
 * Delete/Deactivate a staff user (soft delete)
 */
export async function deleteStaffUser(id: number | string) {
  await api.delete(`/auth/users/${id}/`);
}

/**
 * Activate a staff user
 */
export async function activateStaffUser(id: number | string) {
  const { data } = await api.post<StaffUserDetail>(
    `/auth/users/${id}/activate/`,
  );
  return data;
}

/**
 * Deactivate a staff user
 */
export async function deactivateStaffUser(id: number | string) {
  const { data } = await api.post<StaffUserDetail>(
    `/auth/users/${id}/deactivate/`,
  );
  return data;
}

/**
 * Search staff for autocomplete/select inputs
 * Returns formatted options for react-select or similar components
 */
export async function searchStaff(search: string) {
  if (!search || search.length < 2) {
    return [];
  }

  const response = await getStaff({
    search,
    page: 1,
    page_size: 10,
  });

  return response.results.map((staff) => ({
    value: staff.id,
    label: staff.full_name || staff.email,
    staff, // Include full staff data if needed
  }));
}

/**
 * Get staff by department
 */
export async function getStaffByDepartment(departmentId: number) {
  return getStaff({
    department: departmentId,
    page_size: 100, // Adjust as needed
  });
}

/**
 * Get active staff users only
 */
export async function getActiveStaff() {
  return getStaff({
    is_active: true,
    page_size: 100,
  });
}

/**
 * Bulk operations - Activate multiple staff users
 */
export async function activateStaffUsers(userIds: (number | string)[]) {
  const { data } = await api.post("/auth/users/bulk_activate/", {
    ids: userIds,
  });
  return data;
}

/**
 * Bulk operations - Deactivate multiple staff users
 */
export async function deactivateStaffUsers(userIds: (number | string)[]) {
  const { data } = await api.post("/auth/users/bulk_deactivate/", {
    ids: userIds,
  });
  return data;
}

/**
 * Export staff users (utility function)
 * This would typically trigger a file download
 */
export async function exportStaff(params: StaffListParams = {}) {
  const { data } = await api.get("/auth/users/export/", {
    params,
    responseType: "blob",
  });
  return data;
}

/**
 * Reset staff user password (admin action)
 */
export async function resetStaffPassword(id: number | string) {
  const { data } = await api.post(`/auth/users/${id}/reset_password/`);
  return data;
}
