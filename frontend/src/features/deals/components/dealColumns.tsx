// frontend/src/features/deals/components/dealColumns.tsx

import { column } from "@/components/shared/DataGrid";

import type { Deal } from "../types";

export const dealColumns = [
  column<Deal>({
    accessorKey: "company_name",
    header: "Company",
    width: 200,
  }),

  column<Deal>({
    accessorKey: "contact_name",
    header: "Contact",
    width: 180,
  }),

  column<Deal>({
    accessorKey: "stage",
    header: "Stage",
    width: 160,
  }),

  column<Deal>({
    accessorKey: "amount",
    header: "Amount",
    width: 140,
  }),

  column<Deal>({
    accessorKey: "probability",
    header: "Probability",
    width: 130,
  }),

  column<Deal>({
    accessorKey: "expected_close_date",
    header: "Expected Close",
    width: 170,
  }),

  column<Deal>({
    accessorKey: "owner_name",
    header: "Owner",
    width: 180,
  }),

  column<Deal>({
    accessorKey: "is_active",
    header: "Status",
    width: 120,
  }),
];
