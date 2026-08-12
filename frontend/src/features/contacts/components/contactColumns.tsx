// frontend/src/features/contacts/components/contactColumns.tsx
import { column } from "@/components/shared/DataGrid";

import type { Contact } from "../types";

export const contactColumns = [
  column<Contact>({
    accessorKey: "full_name",
    header: "Name",
    width: 220,
  }),

  column<Contact>({
    accessorKey: "job_title",
    header: "Job Title",
    width: 180,
  }),

  column<Contact>({
    accessorKey: "company_name",
    header: "Company",
    width: 200,
  }),

  column<Contact>({
    accessorKey: "email",
    header: "Email",
    width: 240,
  }),

  column<Contact>({
    accessorKey: "phone",
    header: "Phone",
    width: 160,
  }),

  column<Contact>({
    accessorKey: "mobile",
    header: "Mobile",
    width: 160,
  }),

  column<Contact>({
    accessorKey: "city",
    header: "City",
    width: 140,
  }),

  column<Contact>({
    accessorKey: "country",
    header: "Country",
    width: 140,
  }),
];
