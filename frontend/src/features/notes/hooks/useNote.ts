// frontend/src/features/notes/hooks/useNote.ts
import { useQuery } from "@tanstack/react-query";

import { getNote } from "../api/notesApi";

export function useNote(id: string | undefined) {
  return useQuery({
    queryKey: ["notes", "detail", id],
    queryFn: () => getNote(id!),
    enabled: !!id,
  });
}
