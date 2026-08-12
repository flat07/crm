// frontend/src/features/deals/types.ts
export interface Deal {
  id: number;

  lead: DealLead | null;
  company: DealCompany | null;
  company_name: string | null;

  contact: DealContact | null;
  contact_name: string | null;

  owner: DealOwner | null;
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
export interface DealLead {
  id: number | null;
  title: string | null;
}

export interface DealCompany {
  id: number | null;
  name: string | null;
}

export interface DealContact {
  id: number | null;
  first_name: string | null;
  last_name: string | null;
}

export interface DealOwner {
  id: number | null;
  first_name: string | null;
  last_name: string | null;
}
