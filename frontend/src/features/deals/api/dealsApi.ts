// frontend/src/features/deals/api/dealsApi.ts
import { api } from "@/lib/axios";
import type { PaginatedResponse } from "@/types/api";

import type { Deal } from "../types";

export interface DealListParams {
  page?: number;
  page_size?: number;
  search?: string;
  ordering?: string;
  lead?: number;
  company?: number;
  contact?: number;
  owner?: number;
  stage?: string;
  is_active?: boolean;
}

export async function getDeals(params: DealListParams) {
  const { data } = await api.get<PaginatedResponse<Deal>>("/deals/", {
    params,
  });

  return data;
}

export async function getDeal(id: number) {
  const { data } = await api.get<Deal>(`/deals/${id}/`);

  return data;
}
