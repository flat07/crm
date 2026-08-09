// frontend/src/features/companies/types.ts
import type { BaseModel } from "@/types/common";

export interface Company extends BaseModel {
  name: string;

  legal_name: string;

  website: string;

  email: string;

  phone: string;

  industry: string;

  company_type: string;

  size: string;

  tax_number: string;

  description: string;

  address: string;

  city: string;

  country: string;

  postal_code: string;

  owner: number | null;

  owner_name?: string;

  created_by: number | null;

  created_by_name?: string;

  is_active: boolean;
}
