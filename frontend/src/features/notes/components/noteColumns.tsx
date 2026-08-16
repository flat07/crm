// frontend/src/features/notes/components/noteColumns.tsx

import { column } from "@/components/shared/DataGrid";

import type { Note } from "../types";

function formatDateTime(value: string | null) {
  if (!value) {
    return "—";
  }

  return new Intl.DateTimeFormat("en-US", {
    year: "numeric",
    month: "short",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
  }).format(new Date(value));
}

export const noteColumns = [
  column<Note>({
    accessorKey: "title",
    header: "Title",
    width: 240,
  }),

  column<Note>({
    accessorKey: "content",
    header: "Content",
    width: 320,
  }),

  column<Note>({
    accessorKey: "content_type",
    header: "Related To",
    width: 140,
  }),

  column<Note>({
    accessorKey: "object_display",
    header: "Related Object",
    width: 200,
  }),

  column<Note>({
    accessorKey: "created_by_name",
    header: "Created By",
    width: 180,
  }),

  column<Note>({
    accessorKey: "is_pinned",
    header: "Pinned",
    width: 100,
    cell: ({ row }) => {
      return row.original.is_pinned ? "Yes" : "No";
    },
  }),

  column<Note>({
    accessorKey: "is_private",
    header: "Private",
    width: 100,
    cell: ({ row }) => {
      return row.original.is_private ? "Yes" : "No";
    },
  }),

  column<Note>({
    accessorKey: "created_at",
    header: "Created",
    width: 180,
    cell: ({ row }) => {
      return formatDateTime(row.original.created_at);
    },
  }),
];
