// frontend/src/features/contacts/types/index.ts

export interface Contact {
  id: number;
  first_name: string;
  last_name: string;
  full_name: string;
  job_title: string | null;
  email: string | null;
  phone: string | null;
  mobile: string | null;
  contact_type: string | null;
  source: string | null;
  company: string | null;
  company_name: string | null;
  owner: string | null;
  notes: string | null;
  birthday: string | null; // ISO date string
  linkedin_url: string | null;
  address: string | null;
  city: string | null;
  country: string | null;
  created_at: string;
  updated_at: string;
}

export interface ContactFormData {
  first_name: string;
  last_name: string;
  job_title?: string;
  email?: string;
  phone?: string;
  mobile?: string;
  contact_type?: string;
  source?: string;
  company?: string | null;
  company_name?: string | null;
  owner?: string | null;
  notes?: string;
  birthday?: string;
  linkedin_url?: string;
  address?: string;
  city?: string;
  country?: string;
}

export enum ContactType {
  LEAD = "lead",
  CUSTOMER = "customer",
  PARTNER = "partner",
  SUPPLIER = "supplier",
  OTHER = "other",
}

export enum ContactSource {
  WEBSITE = "website",
  REFERRAL = "referral",
  SOCIAL_MEDIA = "social_media",
  EVENT = "event",
  EMAIL = "email",
  PHONE = "phone",
  OTHER = "other",
}
