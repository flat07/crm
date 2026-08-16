// frontend/src/features/notes/components/NoteCard.tsx

import { Pencil, Pin, Trash2 } from "lucide-react";

import type { Note } from "../types";

interface NoteCardProps {
  note: Note;
  onEdit: (note: Note) => void;
  onDelete: (note: Note) => void;
}

function formatDateTime(value: string) {
  return new Intl.DateTimeFormat("en-US", {
    month: "short",
    day: "numeric",
    year: "numeric",
    hour: "numeric",
    minute: "2-digit",
  }).format(new Date(value));
}

export function NoteCard({ note, onEdit, onDelete }: NoteCardProps) {
  return (
    <article className="rounded-xl border bg-card p-5 shadow-sm">
      <div className="space-y-3">
        {/* Header */}
        <div className="flex items-start justify-between gap-4">
          <div className="min-w-0">
            <div className="flex items-center gap-2">
              <h3 className="truncate font-semibold">
                {note.title || "Untitled note"}
              </h3>

              {note.is_pinned && <Pin className="h-4 w-4 shrink-0" />}
            </div>
          </div>
        </div>

        {/* Content */}
        <p className="whitespace-pre-wrap text-sm text-muted-foreground">
          {note.content}
        </p>

        {/* Related record */}
        {note.object_display && (
          <div className="text-sm">
            <span className="text-muted-foreground">
              {note.content_type.charAt(0).toUpperCase() +
                note.content_type.slice(1)}
              :
            </span>{" "}
            <span className="font-medium">{note.object_display}</span>
          </div>
        )}

        {/* Footer */}
        <div className="flex items-center justify-between gap-4 pt-2">
          <div className="text-xs text-muted-foreground">
            Created {formatDateTime(note.created_at)}
          </div>

          <div className="flex items-center gap-1">
            <button
              type="button"
              onClick={() => onEdit(note)}
              className="inline-flex h-8 items-center gap-1.5 rounded-md px-2.5 text-sm hover:bg-muted"
            >
              <Pencil className="h-4 w-4" />
              Edit
            </button>

            <button
              type="button"
              onClick={() => onDelete(note)}
              className="inline-flex h-8 items-center gap-1.5 rounded-md px-2.5 text-sm text-destructive hover:bg-destructive/10"
            >
              <Trash2 className="h-4 w-4" />
              Delete
            </button>
          </div>
        </div>
      </div>
    </article>
  );
}
