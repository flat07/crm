// frontend/src/features/leads/components/leadFormSchema.ts

import { z } from "zod";

// -----------------------------------------------------------------------------
// Lead choices
// -----------------------------------------------------------------------------

export const leadStatusValues = [
  "new",
  "contacted",
  "qualified",
  "unqualified",
  "converted",
  "archived",
] as const;

export const leadSourceValues = [
  "website",
  "referral",
  "social_media",
  "email",
  "phone",
  "event",
  "advertising",
  "partner",
  "other",
] as const;

// -----------------------------------------------------------------------------
// Labels for UI
// -----------------------------------------------------------------------------

export const leadStatusOptions = [
  { value: "new", label: "New" },
  { value: "contacted", label: "Contacted" },
  { value: "qualified", label: "Qualified" },
  { value: "unqualified", label: "Unqualified" },
  { value: "converted", label: "Converted" },
  { value: "archived", label: "Archived" },
] as const;

export const leadSourceOptions = [
  { value: "website", label: "Website" },
  { value: "referral", label: "Referral" },
  { value: "social_media", label: "Social Media" },
  { value: "email", label: "Email" },
  { value: "phone", label: "Phone" },
  { value: "event", label: "Event" },
  { value: "advertising", label: "Advertising" },
  { value: "partner", label: "Partner" },
  { value: "other", label: "Other" },
] as const;

// -----------------------------------------------------------------------------
// Schema
// -----------------------------------------------------------------------------

export const leadFormSchema = z.object({
  // Basic Information
  title: z.string().min(1, "Title is required"),

  // Relationships
  company: z.uuid().nullable().optional(),
  contact: z.uuid().nullable().optional(),
  owner: z.uuid().nullable().optional(),

  // Lead Details
  source: z.enum(leadSourceValues).nullable().optional(),
  status: z.enum(leadStatusValues),

  // Financial Information
  estimated_value: z
    .string()
    .nullable()
    .optional()
    .transform((val) => (val === "" ? null : val)),

  probability: z
    .number()
    .min(0, "Probability cannot be less than 0")
    .max(100, "Probability cannot be greater than 100"),

  // Dates
  expected_close_date: z.string().nullable().optional(),

  // Additional Information
  description: z.string().nullable().optional().or(z.literal("")),

  // Status
  is_active: z.boolean().default(true),
});

// If you want to handle the estimated_value as a number in the form
export const leadFormSchemaWithNumber = z.object({
  title: z.string().min(1, "Title is required"),

  company: z.uuid().nullable().optional(),
  contact: z.uuid().nullable().optional(),
  owner: z.uuid().nullable().optional(),

  source: z.enum(leadSourceValues).nullable().optional(),
  status: z.enum(leadStatusValues),

  // Alternative: handle estimated_value as number
  estimated_value: z
    .union([
      z.number().min(0, "Estimated value must be positive"),
      z.string().transform((val) => (val === "" ? null : parseFloat(val))),
      z.null(),
    ])
    .optional()
    .nullable(),

  probability: z
    .number()
    .min(0, "Probability cannot be less than 0")
    .max(100, "Probability cannot be greater than 100"),

  expected_close_date: z.string().nullable().optional(),

  description: z.string().nullable().optional().or(z.literal("")),

  is_active: z.boolean().default(true),
});

export type LeadFormInput = z.input<typeof leadFormSchema>;
export type LeadFormValues = z.output<typeof leadFormSchema>;

// If using the number version
export type LeadFormInputWithNumber = z.input<typeof leadFormSchemaWithNumber>;
export type LeadFormValuesWithNumber = z.output<
  typeof leadFormSchemaWithNumber
>;
