// frontend/src/features/companies/components/companyColumns.tsx
import { column } from "@/components/shared/DataGrid";

import type { Company } from "../types";

export const companyColumns = [
  column<Company>({
    accessorKey: "name",
    header: "Name",
    width: 220,
  }),

  column<Company>({
    accessorKey: "industry",
    header: "Industry",
    width: 160,
  }),

  column<Company>({
    accessorKey: "email",
    header: "Email",
    width: 240,
  }),

  column<Company>({
    accessorKey: "phone",
    header: "Phone",
    width: 160,
  }),

  column<Company>({
    accessorKey: "city",
    header: "City",
    width: 140,
  }),

  column<Company>({
    accessorKey: "country",
    header: "Country",
    width: 140,
  }),
];
