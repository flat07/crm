// frontend/src/features/leads/api/leadsApi.ts
import { api } from "@/lib/axios";
import type { PaginatedResponse } from "@/types/api";
import type { Lead, LeadSource, LeadStatus } from "../types";

export interface LeadListParams {
  page?: number;
  page_size?: number;
  search?: string;
  ordering?: string;
  title?: string;
  company?: number;
  company__name?: string;
  contact?: number;
  contact__full_name?: string;
  source?: string;
  status?: LeadStatus | string;
  owner?: number;
  owner__first_name?: string;
  owner__last_name?: string;
  estimated_value_min?: number;
  estimated_value_max?: number;
  probability_min?: number;
  probability_max?: number;
  expected_close_date_after?: string; // ISO date string
  expected_close_date_before?: string; // ISO date string
  is_active?: boolean;
  created_at_after?: string;
  created_at_before?: string;
}

export interface CreateLeadData {
  title: string;
  company?: string | null;
  contact?: string | null;
  source?: LeadSource | null;
  status?: LeadStatus | string;
  estimated_value?: string | number | null;
  probability?: number;
  expected_close_date?: string | null; // ISO date string
  owner?: string | null;
  description?: string | null;
  is_active?: boolean;
}

export type UpdateLeadData = Partial<CreateLeadData>;

/**
 * Get paginated list of leads with optional filters
 */
export async function getLeads(params: LeadListParams = {}) {
  const { data } = await api.get<PaginatedResponse<Lead>>("/leads/", {
    params,
  });
  return data;
}

/**
 * Get a single lead by ID
 */
export async function getLead(id: string) {
  const { data } = await api.get<Lead>(`/leads/${id}/`);
  return data;
}

/**
 * Create a new lead
 */
export async function createLead(leadData: CreateLeadData) {
  const { data } = await api.post<Lead>("/leads/", leadData);
  return data;
}

/**
 * Update an existing lead
 */
export async function updateLead(id: string, leadData: UpdateLeadData) {
  const { data } = await api.patch<Lead>(`/leads/${id}/`, leadData);
  return data;
}

/**
 * Delete/archive a lead (soft delete)
 */
export async function deleteLead(id: string) {
  await api.delete(`/leads/${id}/`);
}

/**
 * Restore an archived lead
 */
export async function restoreLead(id: string) {
  const { data } = await api.post<Lead>(`/leads/${id}/restore/`);
  return data;
}

/**
 * Permanently delete a lead (hard delete)
 */
export async function hardDeleteLead(id: string) {
  await api.delete(`/leads/${id}/hard_delete/`);
}

/**
 * Convert a lead to a deal
 */
export async function convertLeadToDeal(
  id: string,
  dealData?: {
    stage?: string;
    amount?: string | number;
    expected_close_date?: string;
  },
) {
  const { data } = await api.post<Lead>(
    `/leads/${id}/convert/`,
    dealData || {},
  );
  return data;
}

/**
 * Search leads for autocomplete/select inputs
 * Returns formatted options for react-select or similar components
 */
export async function searchLeads(search: string) {
  if (!search || search.length < 2) {
    return [];
  }

  const response = await getLeads({
    search,
    page: 1,
    page_size: 10,
  });

  return response.results.map((lead) => ({
    value: lead.id,
    label: lead.title,
    lead, // Include full lead data if needed
  }));
}

/**
 * Get leads by company ID
 */
export async function getLeadsByCompany(companyId: number) {
  return getLeads({
    company: companyId,
    page_size: 100, // Adjust as needed
  });
}

/**
 * Get leads by contact ID
 */
export async function getLeadsByContact(contactId: number) {
  return getLeads({
    contact: contactId,
    page_size: 100,
  });
}

/**
 * Get leads by owner ID
 */
export async function getLeadsByOwner(ownerId: number) {
  return getLeads({
    owner: ownerId,
    page_size: 100,
  });
}

/**
 * Get leads by status
 */
export async function getLeadsByStatus(status: LeadStatus) {
  return getLeads({
    status,
    page_size: 100,
  });
}

/**
 * Get active leads only
 */
export async function getActiveLeads() {
  return getLeads({
    is_active: true,
    page_size: 100,
  });
}

/**
 * Bulk operations - Archive multiple leads
 */
export async function archiveLeads(leadIds: number[]) {
  const { data } = await api.post("/leads/bulk_archive/", {
    ids: leadIds,
  });
  return data;
}

/**
 * Bulk operations - Delete multiple leads permanently
 */
export async function hardDeleteLeads(leadIds: number[]) {
  const { data } = await api.post("/leads/bulk_hard_delete/", {
    ids: leadIds,
  });
  return data;
}

/**
 * Bulk operations - Update status for multiple leads
 */
export async function bulkUpdateLeadStatus(
  leadIds: number[],
  status: LeadStatus,
) {
  const { data } = await api.post("/leads/bulk_update_status/", {
    ids: leadIds,
    status,
  });
  return data;
}

/**
 * Export leads (utility function)
 * This would typically trigger a file download
 */
export async function exportLeads(params: LeadListParams = {}) {
  const { data } = await api.get("/leads/export/", {
    params,
    responseType: "blob",
  });
  return data;
}

/**
 * Get lead statistics/summary
 */
export async function getLeadStats() {
  const { data } = await api.get("/leads/stats/");
  return data;
}
