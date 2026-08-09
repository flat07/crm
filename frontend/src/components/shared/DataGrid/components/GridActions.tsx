import { Eye, MoreHorizontal, Pencil, Trash2 } from "lucide-react";

import { useState } from "react";

import type { DataGridActions } from "../types";

interface GridActionsProps<TData> {
  row: TData;

  actions?: DataGridActions<TData>;

  onView(row: TData): void;

  onEdit(row: TData): void;
}

export function GridActions<TData>({
  row,
  actions,
  onView,
  onEdit,
}: GridActionsProps<TData>) {
  const [loading, setLoading] = useState(false);

  const [open, setOpen] = useState(false);

  if (!actions) {
    return null;
  }

  const hasActions = actions.view || actions.edit || actions.delete;

  if (!hasActions) {
    return null;
  }

  async function handleDelete() {
    if (!actions?.onDelete) {
      return;
    }

    const confirmed = window.confirm(
      "Are you sure you want to delete this item?",
    );

    if (!confirmed) {
      return;
    }

    try {
      setLoading(true);

      await actions.onDelete(row);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div
      className="relative flex justify-end"
      onClick={(event) => event.stopPropagation()}
    >
      <button
        type="button"
        onClick={() => setOpen((previous) => !previous)}
        className="inline-flex h-8 w-8 items-center justify-center rounded-md hover:bg-muted"
      >
        <MoreHorizontal className="h-4 w-4" />
      </button>

      {open && (
        <div className="absolute right-0 top-9 z-30 min-w-36 overflow-hidden rounded-lg border bg-background py-1 shadow-lg">
          {actions.view && (
            <button
              type="button"
              onClick={() => {
                setOpen(false);

                onView(row);
              }}
              className="flex w-full items-center gap-2 px-3 py-2 text-sm hover:bg-muted"
            >
              <Eye className="h-4 w-4" />
              View
            </button>
          )}

          {actions.edit && (
            <button
              type="button"
              onClick={() => {
                setOpen(false);

                onEdit(row);
              }}
              className="flex w-full items-center gap-2 px-3 py-2 text-sm hover:bg-muted"
            >
              <Pencil className="h-4 w-4" />
              Edit
            </button>
          )}

          {actions.delete && (
            <button
              type="button"
              disabled={loading}
              onClick={handleDelete}
              className="flex w-full items-center gap-2 px-3 py-2 text-sm text-destructive hover:bg-muted disabled:opacity-50"
            >
              <Trash2 className="h-4 w-4" />

              {loading ? "Deleting..." : "Delete"}
            </button>
          )}
        </div>
      )}
    </div>
  );
}
