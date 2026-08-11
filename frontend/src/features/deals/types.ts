export interface Deal {
  id: number;

  lead: number | null;
  company: number | null;
  company_name: string | null;

  contact: number | null;
  contact_name: string | null;

  owner: string | null;
  owner_name: string | null;

  stage: string;

  amount: string;
  probability: number;

  expected_close_date: string | null;
  actual_close_date: string | null;

  description: string;

  is_active: boolean;

  created_at: string;
  updated_at: string;
}
