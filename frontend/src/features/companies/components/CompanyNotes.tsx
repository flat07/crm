import { useState } from "react";

import { Button } from "@/components/ui/button";

import { useNotes } from "@/features/notes/hooks/useNotes";
import { RelatedNoteForm } from "./RelatedNoteForm";

interface CompanyNotesProps {
  companyId: string;
}

export function CompanyNotes({ companyId }: CompanyNotesProps) {
  const [showForm, setShowForm] = useState(false);

  const { data, isLoading, isError } = useNotes({
    content_type: "company",
    object_id: companyId,
  });

  if (isLoading) {
    return (
      <section className="space-y-4">
        <h3 className="text-sm font-semibold">Notes</h3>

        <p className="text-sm text-muted-foreground">Loading notes...</p>
      </section>
    );
  }

  if (isError) {
    return (
      <section className="space-y-4">
        <h3 className="text-sm font-semibold">Notes</h3>

        <p className="text-sm text-destructive">Failed to load notes.</p>
      </section>
    );
  }

  const notes = data?.results ?? [];

  return (
    <section className="space-y-4">
      {/* Header */}
      <div className="flex items-start justify-between gap-4">
        <div>
          <h3 className="text-sm font-semibold">Notes</h3>

          <p className="text-sm text-muted-foreground">
            Notes and important information about this company.
          </p>
        </div>

        <Button
          type="button"
          size="sm"
          onClick={() => setShowForm((value) => !value)}
        >
          {showForm ? "Cancel" : "Add note"}
        </Button>
      </div>

      {/* Create note form */}
      {showForm && (
        <div className="rounded-lg border p-4">
          <RelatedNoteForm
            contentType="company"
            objectId={companyId}
            onSuccess={() => {
              setShowForm(false);
            }}
            onCancel={() => {
              setShowForm(false);
            }}
          />
        </div>
      )}

      {/* Notes */}
      {notes.length === 0 ? (
        <div className="rounded-lg border p-6 text-center">
          <p className="text-sm text-muted-foreground">No notes yet.</p>
        </div>
      ) : (
        <div className="space-y-3">
          {notes.map((note) => (
            <div key={note.id} className="rounded-lg border p-4">
              <div className="flex items-start justify-between gap-4">
                <div className="min-w-0">
                  {note.title && (
                    <h4 className="text-sm font-medium">{note.title}</h4>
                  )}

                  <p className="mt-1 whitespace-pre-wrap text-sm">
                    {note.content}
                  </p>
                </div>

                <div className="flex shrink-0 items-center gap-2">
                  {note.is_pinned && (
                    <span className="text-xs text-muted-foreground">
                      Pinned
                    </span>
                  )}

                  {note.is_private && (
                    <span className="text-xs text-muted-foreground">
                      Private
                    </span>
                  )}
                </div>
              </div>

              <div className="mt-3 text-xs text-muted-foreground">
                {note.created_by_name}
              </div>
            </div>
          ))}
        </div>
      )}
    </section>
  );
}
