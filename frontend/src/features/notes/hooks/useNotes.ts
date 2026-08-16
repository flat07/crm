// frontend/src/features/notes/hooks/useNotes.ts
import { useQuery } from "@tanstack/react-query";

import { getNotes } from "../api/notesApi";
import type { NoteListParams } from "../types";

export function useNotes(params: NoteListParams) {
  return useQuery({
    queryKey: ["notes", "list", params],
    queryFn: () => getNotes(params),
  });
}
