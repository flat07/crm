// frontend/src/features/companies/components/companyFormSchema.ts

import { z } from "zod";

// -----------------------------------------------------------------------------
// Company choices
// -----------------------------------------------------------------------------

export const industryValues = [
  "technology",
  "finance",
  "healthcare",
  "education",
  "hospitality",
  "retail",
  "other",
] as const;

export const companyTypeValues = [
  "customer",
  "partner",
  "vendor",
  "prospect",
] as const;

export const companySizeValues = [
  "small",
  "medium",
  "large",
  "enterprise",
] as const;

// -----------------------------------------------------------------------------
// Labels for UI
// -----------------------------------------------------------------------------

export const industryOptions = [
  { value: "technology", label: "Technology" },
  { value: "finance", label: "Finance" },
  { value: "healthcare", label: "Healthcare" },
  { value: "education", label: "Education" },
  { value: "hospitality", label: "Hospitality" },
  { value: "retail", label: "Retail" },
  { value: "other", label: "Other" },
] as const;

export const companyTypeOptions = [
  { value: "customer", label: "Customer" },
  { value: "partner", label: "Partner" },
  { value: "vendor", label: "Vendor" },
  { value: "prospect", label: "Prospect" },
] as const;

export const companySizeOptions = [
  { value: "small", label: "Small" },
  { value: "medium", label: "Medium" },
  { value: "large", label: "Large" },
  { value: "enterprise", label: "Enterprise" },
] as const;

// -----------------------------------------------------------------------------
// Schema
// -----------------------------------------------------------------------------

export const companyFormSchema = z.object({
  name: z.string().min(1, "Company name is required").max(255),

  legal_name: z.string().max(255).optional().or(z.literal("")),

  website: z.string().url("Invalid website URL").optional().or(z.literal("")),

  email: z.string().email("Invalid email address").optional().or(z.literal("")),

  phone: z.string().max(20).optional().or(z.literal("")),

  industry: z.enum(industryValues).optional().or(z.literal("")),

  company_type: z.enum(companyTypeValues).optional().or(z.literal("")),

  size: z.enum(companySizeValues).optional().or(z.literal("")),

  tax_number: z.string().max(100).optional().or(z.literal("")),

  description: z.string().optional().or(z.literal("")),

  address: z.string().optional().or(z.literal("")),

  city: z.string().max(100).optional().or(z.literal("")),

  country: z.string().max(100).optional().or(z.literal("")),

  postal_code: z.string().max(20).optional().or(z.literal("")),

  owner: z.string().uuid().nullable().optional(),

  is_active: z.boolean().default(true),
});

export type CompanyFormInput = z.input<typeof companyFormSchema>;

export type CompanyFormValues = z.output<typeof companyFormSchema>;
