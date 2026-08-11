// frontend/src/features/contacts/api/contactApi.ts
import { api } from "@/lib/axios";
import type { PaginatedResponse } from "@/types/api";
import type { Contact } from "../types";

export interface ContactListParams {
  page?: number;
  page_size?: number;
  search?: string;
  ordering?: string;
  first_name?: string;
  last_name?: string;
  email?: string;
  phone?: string;
  mobile?: string;
  job_title?: string;
  company?: number;
  company__name?: string;
  owner?: number;
  owner__first_name?: string;
  owner__last_name?: string;
  city?: string;
  country?: string;
  contact_type?: string;
  source?: string;
  created_at_after?: string;
  created_at_before?: string;
  birthday_after?: string;
  birthday_before?: string;
}

export interface CreateContactData {
  first_name: string;
  last_name: string;
  job_title?: string;
  email?: string;
  phone?: string;
  mobile?: string;
  contact_type?: string;
  source?: string;
  company?: number;
  owner?: number;
  notes?: string;
  birthday?: string; // ISO date string
  linkedin_url?: string;
  address?: string;
  city?: string;
  country?: string;
}

export type UpdateContactData = Partial<CreateContactData>;

/**
 * Get paginated list of contacts with optional filters
 */
export async function getContacts(params: ContactListParams = {}) {
  const { data } = await api.get<PaginatedResponse<Contact>>("/contacts/", {
    params,
  });
  return data;
}

/**
 * Get a single contact by ID
 */
export async function getContact(id: number) {
  const { data } = await api.get<Contact>(`/contacts/${id}/`);
  return data;
}

/**
 * Create a new contact
 */
export async function createContact(contactData: CreateContactData) {
  const { data } = await api.post<Contact>("/contacts/", contactData);
  return data;
}

/**
 * Update an existing contact
 */
export async function updateContact(
  id: number,
  contactData: UpdateContactData,
) {
  const { data } = await api.patch<Contact>(`/contacts/${id}/`, contactData);
  return data;
}

/**
 * Delete/archive a contact (soft delete)
 */
export async function deleteContact(id: number) {
  await api.delete(`/contacts/${id}/`);
}

/**
 * Restore an archived contact
 */
export async function restoreContact(id: number) {
  const { data } = await api.post<Contact>(`/contacts/${id}/restore/`);
  return data;
}

/**
 * Permanently delete a contact (hard delete)
 */
export async function hardDeleteContact(id: number) {
  await api.delete(`/contacts/${id}/hard_delete/`);
}

/**
 * Search contacts for autocomplete/select inputs
 * Returns formatted options for react-select or similar components
 */
export async function searchContacts(search: string) {
  if (!search || search.length < 2) {
    return [];
  }

  const response = await getContacts({
    search,
    page: 1,
    page_size: 10,
  });

  return response.results.map((contact) => ({
    value: contact.id,
    label: contact.full_name || `${contact.first_name} ${contact.last_name}`,
    contact, // Include full contact data if needed
  }));
}

/**
 * Get contacts by company ID
 */
export async function getContactsByCompany(companyId: number) {
  return getContacts({
    company: companyId,
    page_size: 100, // Adjust as needed
  });
}

/**
 * Get contacts by owner ID
 */
export async function getContactsByOwner(ownerId: number) {
  return getContacts({
    owner: ownerId,
    page_size: 100, // Adjust as needed
  });
}

/**
 * Export contacts (utility function)
 * This would typically trigger a file download
 */
export async function exportContacts(params: ContactListParams = {}) {
  const { data } = await api.get("/contacts/export/", {
    params,
    responseType: "blob",
  });
  return data;
}

/**
 * Bulk operations - Archive multiple contacts
 */
export async function archiveContacts(contactIds: number[]) {
  const { data } = await api.post("/contacts/bulk_archive/", {
    ids: contactIds,
  });
  return data;
}

/**
 * Bulk operations - Delete multiple contacts permanently
 */
export async function hardDeleteContacts(contactIds: number[]) {
  const { data } = await api.post("/contacts/bulk_hard_delete/", {
    ids: contactIds,
  });
  return data;
}
