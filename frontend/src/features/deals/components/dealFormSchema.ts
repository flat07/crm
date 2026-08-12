// frontend/src/features/deals/components/dealFormSchema.ts
import { z } from "zod";

// -----------------------------------------------------------------------------
// Deal choices
// -----------------------------------------------------------------------------

export const dealStageValues = [
  "prospecting",
  "discovery",
  "proposal",
  "negotiation",
  "contract",
  "won",
  "lost",
] as const;

// -----------------------------------------------------------------------------
// Labels for UI
// -----------------------------------------------------------------------------

export const dealStageOptions = [
  { value: "prospecting", label: "Prospecting" },
  { value: "discovery", label: "Discovery" },
  { value: "proposal", label: "Proposal" },
  { value: "negotiation", label: "Negotiation" },
  { value: "contract", label: "Contract" },
  { value: "won", label: "Won" },
  { value: "lost", label: "Lost" },
] as const;

// -----------------------------------------------------------------------------
// Schema
// -----------------------------------------------------------------------------

export const dealFormSchema = z.object({
  lead: z.uuid().nullable(),

  company: z.uuid().nullable(),

  contact: z.uuid().nullable(),

  owner: z.uuid().nullable().optional(),

  stage: z.enum(dealStageValues),

  amount: z.string().min(1, "Amount is required"),

  probability: z
    .number()
    .min(0, "Probability cannot be less than 0")
    .max(100, "Probability cannot be greater than 100"),

  expected_close_date: z.string().nullable().optional(),

  actual_close_date: z.string().nullable().optional(),

  description: z.string().optional().or(z.literal("")),

  is_active: z.boolean().default(true),
});

export type DealFormInput = z.input<typeof dealFormSchema>;

export type DealFormValues = z.output<typeof dealFormSchema>;
