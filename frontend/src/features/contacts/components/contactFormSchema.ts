// frontend/src/features/contacts/components/contactFormSchema.ts
import { z } from "zod";

// -----------------------------------------------------------------------------
// Contact choices
// -----------------------------------------------------------------------------

export const contactTypeValues = [
  "customer",
  "lead",
  "partner",
  "vendor",
] as const;

export const contactSourceValues = [
  "website",
  "referral",
  "social_media",
  "email",
  "phone",
  "event",
  "other",
] as const;

// -----------------------------------------------------------------------------
// Labels for UI
// -----------------------------------------------------------------------------

export const contactTypeOptions = [
  { value: "customer", label: "Customer" },
  { value: "lead", label: "Lead" },
  { value: "partner", label: "Partner" },
  { value: "vendor", label: "Vendor" },
] as const;

export const contactSourceOptions = [
  { value: "website", label: "Website" },
  { value: "referral", label: "Referral" },
  { value: "social_media", label: "Social Media" },
  { value: "email", label: "Email" },
  { value: "phone", label: "Phone" },
  { value: "event", label: "Event" },
  { value: "other", label: "Other" },
] as const;

// -----------------------------------------------------------------------------
// Schema
// -----------------------------------------------------------------------------

export const contactFormSchema = z.object({
  first_name: z.string().min(1, "First name is required").max(100),

  last_name: z.string().min(1, "Last name is required").max(100),

  job_title: z.string().max(255).optional().or(z.literal("")),

  email: z.string().email("Invalid email address").optional().or(z.literal("")),

  phone: z.string().max(20).optional().or(z.literal("")),

  mobile: z.string().max(20).optional().or(z.literal("")),

  contact_type: z.enum(contactTypeValues).optional().or(z.literal("")),

  source: z.enum(contactSourceValues).optional().or(z.literal("")),

  company_id: z.string().uuid().nullable().optional(),

  owner_id: z.string().uuid().nullable().optional(),

  notes: z.string().optional().or(z.literal("")),

  birthday: z
    .string()
    .transform((value) => (value === "" ? null : value))
    .nullable(),

  linkedin_url: z
    .string()
    .url("Invalid LinkedIn URL")
    .optional()
    .or(z.literal("")),

  address: z.string().optional().or(z.literal("")),

  city: z.string().max(100).optional().or(z.literal("")),

  country: z.string().max(100).optional().or(z.literal("")),
});

// -----------------------------------------------------------------------------
// Types
// -----------------------------------------------------------------------------

export type ContactFormInput = z.input<typeof contactFormSchema>;

export type ContactFormValues = z.output<typeof contactFormSchema>;
