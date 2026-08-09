// frontend/src/features/companies/api/companyMutations.ts
import { api } from "@/lib/axios";

import type { Company } from "../types";

import type { CompanyFormValues } from "../components/companyFormSchema";

export async function createCompany(values: CompanyFormValues) {
  const { data } = await api.post<Company>("/companies/", values);

  return data;
}

export async function updateCompany(id: number, values: CompanyFormValues) {
  const { data } = await api.patch<Company>(`/companies/${id}/`, values);

  return data;
}

export async function deleteCompany(id: number) {
  await api.delete(`/companies/${id}/`);
}
