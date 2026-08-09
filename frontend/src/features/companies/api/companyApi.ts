// frontend/src/features/companies/api/companyApi.ts
import { api } from "@/lib/axios";
import type { PaginatedResponse } from "@/types/api";
import type { Company } from "../types";

export interface CompanyListParams {
  page?: number;
  page_size?: number;
  search?: string;
  ordering?: string;
  industry?: string;
}

export async function getCompanies(params: CompanyListParams) {
  const { data } = await api.get<PaginatedResponse<Company>>("/companies/", {
    params,
  });
  // console.log("companyApi.ts: params: ", params);
  // console.log("DEBUG: getCompanies: data ", data);

  return data;
}

export async function getCompany(id: number) {
  const { data } = await api.get<Company>(`/companies/${id}/`);

  return data;
}
