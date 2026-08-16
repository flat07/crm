// frontend/src/features/notes/api/notesApi.ts

import { api } from "@/lib/axios";

import type { PaginatedResponse } from "@/types/pagination";
import type {
  Note,
  NoteCreateInput,
  NoteDetail,
  NoteUpdateInput,
} from "../types";
import { NoteListParams } from "../types";

/**
 * Get notes
 */
export async function getNotes(
  params: NoteListParams,
): Promise<PaginatedResponse<Note>> {
  const { data } = await api.get<PaginatedResponse<Note>>("/notes/", {
    params,
  });

  return data;
}

/**
 * Get a single note
 */
export async function getNote(id: string): Promise<NoteDetail> {
  const { data } = await api.get<NoteDetail>(`/notes/${id}/`);

  return data;
}

/**
 * Create a note
 */
export async function createNote(values: NoteCreateInput): Promise<NoteDetail> {
  const { data } = await api.post<NoteDetail>("/notes/", values);

  return data;
}

/**
 * Update a note
 */
export async function updateNote(
  id: string,
  values: Partial<NoteUpdateInput>,
): Promise<NoteDetail> {
  const { data } = await api.patch<NoteDetail>(`/notes/${id}/`, values);

  return data;
}

/**
 * Delete a note
 */
export async function deleteNote(id: string): Promise<void> {
  await api.delete(`/notes/${id}/`);
}
