// frontend/src/features/notes/types.ts
// frontend/src/features/notes/types.ts

export type NoteContentType = "company" | "contact" | "lead" | "deal";

export interface NoteContentObject {
  id: string;
  type: string;
  display: string;
}

export interface Note {
  id: string;
  title: string;
  content: string;

  content_type: NoteContentType;
  object_id: string | number | null;
  object_display: string | null;

  created_by: string;
  created_by_name: string;

  is_pinned: boolean;
  is_private: boolean;

  created_at: string;
  updated_at: string;
}

export interface NoteDetail {
  id: string;
  title: string;
  content: string;

  created_by: string;

  is_pinned: boolean;
  is_private: boolean;

  content_type: NoteContentType;
  object_id: string | number | null;

  content_object: NoteContentObject | null;

  created_at: string;
  updated_at: string;
}

export interface NoteCreateInput {
  title: string;
  content: string;

  content_type: NoteContentType;
  object_id: string | number;

  is_pinned?: boolean;
  is_private?: boolean;
}

export interface NoteUpdateInput {
  title?: string;
  content?: string;

  content_type?: NoteContentType;
  object_id?: string | number;

  is_pinned?: boolean;
  is_private?: boolean;
}

export interface NoteListParams {
  page?: number;
  page_size?: number;
  search?: string;
  ordering?: string;
  content_type?: NoteContentType;
  object_id?: string | number;
}
