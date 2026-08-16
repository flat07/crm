// frontend/src/features/notes/hooks/useUpdateNote.ts

import { useMutation, useQueryClient } from "@tanstack/react-query";

import { updateNote } from "../api/notesApi";
import type { NoteUpdateInput } from "../types";

interface UpdateNoteVariables {
  id: string;
  values: Partial<NoteUpdateInput>;
}

export function useUpdateNote() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ id, values }: UpdateNoteVariables) => updateNote(id, values),

    onSuccess: (_, variables) => {
      queryClient.invalidateQueries({
        queryKey: ["notes"],
      });

      queryClient.invalidateQueries({
        queryKey: ["notes", "detail", variables.id],
      });
    },
  });
}
