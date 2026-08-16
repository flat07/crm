// frontend/src/features/notes/components/noteFormSchema.ts

import { z } from "zod";

// -----------------------------------------------------------------------------
// Note choices
// -----------------------------------------------------------------------------

export const noteContentTypeValues = [
  "company",
  "contact",
  "lead",
  "deal",
] as const;

// -----------------------------------------------------------------------------
// Labels for UI
// -----------------------------------------------------------------------------

export const noteContentTypeOptions = [
  { value: "company", label: "Company" },
  { value: "contact", label: "Contact" },
  { value: "lead", label: "Lead" },
  { value: "deal", label: "Deal" },
] as const;

// -----------------------------------------------------------------------------
// Schema
// -----------------------------------------------------------------------------

export const noteFormSchema = z.object({
  title: z.string().max(255).optional().or(z.literal("")),

  content: z.string().min(1, "Content is required"),

  content_type: z.enum(noteContentTypeValues),

  object_id: z.string().min(1, "Related object is required"),

  is_pinned: z.boolean().default(false),

  is_private: z.boolean().default(false),
});

// -----------------------------------------------------------------------------
// Types
// -----------------------------------------------------------------------------

export type NoteFormInput = z.input<typeof noteFormSchema>;

export type NoteFormValues = z.output<typeof noteFormSchema>;
