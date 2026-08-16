// frontend/src/features/notes/pages/NotesPage.tsx

import { useState } from "react";

import { NoteCard } from "../components/NoteCard";
import { NoteDrawer } from "../components/NoteDrawer";
import { NotesToolbar } from "../components/NotesToolbar";

import { useCreateNote } from "../hooks/useCreateNote";
import { useDeleteNote } from "../hooks/useDeleteNote";
import { useNotes } from "../hooks/useNotes";
import { useUpdateNote } from "../hooks/useUpdateNote";

import type { NoteFormValues } from "../components/noteFormSchema";
import type { Note } from "../types";

export function NotesPage() {
  const [search, setSearch] = useState("");
  const [drawerOpen, setDrawerOpen] = useState(false);
  const [selectedNote, setSelectedNote] = useState<Note | null>(null);

  const { data, isLoading, isError } = useNotes({
    page: 1,
    page_size: 50,
    search,
  });

  const createMutation = useCreateNote();
  const updateMutation = useUpdateNote();
  const deleteMutation = useDeleteNote();

  const notes = data?.results ?? [];

  const handleAdd = () => {
    setSelectedNote(null);
    setDrawerOpen(true);
  };

  const handleEdit = (note: Note) => {
    setSelectedNote(note);
    setDrawerOpen(true);
  };

  const handleDelete = async (note: Note) => {
    const confirmed = window.confirm(
      `Delete "${note.title || "Untitled note"}"?`,
    );

    if (!confirmed) {
      return;
    }

    await deleteMutation.mutateAsync(note.id);
  };

  const handleSubmit = async (values: NoteFormValues) => {
    const payload = {
      ...values,
      title: values.title || "",
    };
    if (selectedNote) {
      await updateMutation.mutateAsync({
        id: selectedNote.id,
        values: payload,
      });
    } else {
      await createMutation.mutateAsync(payload);
    }

    setDrawerOpen(false);
    setSelectedNote(null);
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div>
        <h1 className="text-2xl font-semibold">Notes</h1>

        <p className="text-sm text-muted-foreground">
          Keep track of important CRM notes.
        </p>
      </div>

      {/* Toolbar */}
      <NotesToolbar
        search={search}
        onSearchChange={setSearch}
        onAdd={handleAdd}
      />

      {/* Loading */}
      {isLoading && (
        <div className="py-12 text-center text-sm text-muted-foreground">
          Loading notes...
        </div>
      )}

      {/* Error */}
      {isError && (
        <div className="rounded-lg border border-destructive/30 p-6 text-center text-sm text-destructive">
          Failed to load notes.
        </div>
      )}

      {/* Empty */}
      {!isLoading && !isError && notes.length === 0 && (
        <div className="rounded-xl border border-dashed p-12 text-center">
          <h3 className="font-medium">No notes found</h3>

          <p className="mt-1 text-sm text-muted-foreground">
            Create your first note to get started.
          </p>
        </div>
      )}

      {/* Notes */}
      {!isLoading && !isError && notes.length > 0 && (
        <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
          {notes.map((note) => (
            <NoteCard
              key={note.id}
              note={note}
              onEdit={handleEdit}
              onDelete={handleDelete}
            />
          ))}
        </div>
      )}

      {/* Drawer */}
      <NoteDrawer
        open={drawerOpen}
        note={selectedNote}
        onClose={() => {
          setDrawerOpen(false);
          setSelectedNote(null);
        }}
        onSubmit={handleSubmit}
      />
    </div>
  );
}
