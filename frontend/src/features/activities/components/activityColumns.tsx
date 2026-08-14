import { column } from "@/components/shared/DataGrid";

import type { Activity } from "../types";

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

export const activityColumns = [
  column<Activity>({
    accessorKey: "title",
    header: "Title",
    width: 240,
  }),

  column<Activity>({
    accessorKey: "activity_type",
    header: "Type",
    width: 130,
  }),

  column<Activity>({
    accessorKey: "status",
    header: "Status",
    width: 150,
  }),

  column<Activity>({
    accessorKey: "priority",
    header: "Priority",
    width: 130,
  }),

  column<Activity>({
    accessorKey: "due_date",
    header: "Due Date",
    width: 180,
    cell: ({ row }) => {
      const value = row.original.due_date;

      return formatDateTime(value);
    },
  }),

  column<Activity>({
    accessorKey: "owner_name",
    header: "Owner",
    width: 180,
  }),

  column<Activity>({
    accessorKey: "content_type",
    header: "Related To",
    width: 140,
  }),

  column<Activity>({
    accessorKey: "created_at",
    header: "Created",
    width: 180,
    cell: ({ row }) => {
      const value = row.original.created_at;

      return formatDateTime(value);
    },
  }),
];
