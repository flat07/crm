// frontend/src/features/deals/api/dealsMutations.ts
import { api } from "@/lib/axios";

import type { DealFormValues } from "../components/dealFormSchema";
import type { Deal } from "../types";

export async function createDeal(values: DealFormValues) {
  console.log("DEBUG: dealsMutations values:", values);

  try {
    const response = await api.post<Deal>("/deals/", values);

    // console.log("DEBUG: dealsMutations response:", response);
    // console.log("DEBUG: dealsMutations data:", response.data);

    return response.data;
  } catch (error) {
    // console.error("DEBUG: dealsMutations ERROR:", error);

    if (error instanceof Error) {
      console.error("DEBUG: dealsMutations message:", error.message);
    }

    throw error;
  }
}
export async function updateDeal(id: string, values: DealFormValues) {
  const { data } = await api.patch<Deal>(`/deals/${id}/`, values);

  return data;
}

export async function deleteDeal(id: string) {
  await api.delete(`/deals/${id}/`);
}
