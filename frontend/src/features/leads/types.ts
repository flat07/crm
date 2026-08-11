// frontend/src/features/leads/types/index.ts

export type LeadStatus =
  "new" | "contacted" | "qualified" | "unqualified" | "converted" | "archived";

export type LeadSource =
  | "website"
  | "referral"
  | "social_media"
  | "email"
  | "phone"
  | "event"
  | "advertising"
  | "partner"
  | "other";

export interface Lead {
  id: number;
  title: string;
  company: number | null;
  company_detail?: {
    id: number;
    name: string;
  };
  contact: number | null;
  contact_detail?: {
    id: number;
    full_name: string;
  };
  source: LeadSource | null;
  status: LeadStatus;
  estimated_value: string | null; // Decimal field
  probability: number;
  expected_close_date: string | null; // ISO date string
  owner: number | null;
  owner_detail?: {
    id: number;
    full_name: string;
    email: string;
  };
  description: string | null;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface LeadFormData {
  title: string;
  company: number | null;
  contact: number | null;
  source: LeadSource | null;
  status: LeadStatus;
  estimated_value: string | number | null;
  probability: number;
  expected_close_date: string | null;
  owner: number | null;
  description: string | null;
  is_active: boolean;
}

export interface LeadFilters {
  search?: string;
  status?: LeadStatus | LeadStatus[];
  source?: LeadSource | LeadSource[];
  company?: number;
  contact?: number;
  owner?: number;
  estimated_value_min?: number;
  estimated_value_max?: number;
  probability_min?: number;
  probability_max?: number;
  expected_close_date_after?: string;
  expected_close_date_before?: string;
  is_active?: boolean;
  created_at_after?: string;
  created_at_before?: string;
  ordering?: string;
}

export interface LeadStats {
  total: number;
  by_status: {
    [key in LeadStatus]: number;
  };
  by_source: {
    [key in LeadSource]: number;
  };
  total_estimated_value: number;
  average_probability: number;
  conversion_rate: number;
}
