// frontend/src/features/notes/hooks/useDeleteNote.ts
import { useMutation, useQueryClient } from "@tanstack/react-query";

import { deleteNote } from "../api/notesApi";

export function useDeleteNote() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (id: string) => deleteNote(id),

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["notes"],
      });
    },
  });
}
