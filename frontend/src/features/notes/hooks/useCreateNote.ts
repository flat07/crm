// frontend/src/features/notes/hooks/useCreateNote.ts

import { useMutation, useQueryClient } from "@tanstack/react-query";

import { createNote } from "../api/notesApi";
import type { NoteCreateInput } from "../types";

export function useCreateNote() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (values: NoteCreateInput) => createNote(values),

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["notes"],
      });
    },
  });
}
