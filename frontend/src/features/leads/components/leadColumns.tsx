// frontend/src/features/leads/components/leadColumns.tsx

import { column } from "@/components/shared/DataGrid";

import type { Lead } from "../types";

export const leadColumns = [
  column<Lead>({
    accessorKey: "title",
    header: "Lead Title",
    width: 200,
  }),

  column<Lead>({
    accessorKey: "company_name",
    header: "Company",
    width: 200,
  }),

  column<Lead>({
    accessorKey: "contact_name",
    header: "Contact",
    width: 180,
  }),

  column<Lead>({
    accessorKey: "status",
    header: "Status",
    width: 140,
  }),

  column<Lead>({
    accessorKey: "source",
    header: "Source",
    width: 140,
  }),

  column<Lead>({
    accessorKey: "estimated_value",
    header: "Estimated Value",
    width: 150,
  }),

  column<Lead>({
    accessorKey: "probability",
    header: "Probability",
    width: 130,
  }),

  column<Lead>({
    accessorKey: "expected_close_date",
    header: "Expected Close",
    width: 170,
  }),

  column<Lead>({
    accessorKey: "owner_name",
    header: "Owner",
    width: 180,
  }),

  column<Lead>({
    accessorKey: "is_active",
    header: "Is Active",
    width: 120,
  }),
];
