// frontend/src/features/leads/api/leadEntitySearch.ts
import { getLeads } from "./leadsApi";

export async function searchLeads(search: string) {
  const response = await getLeads({
    search,
    page: 1,
    page_size: 10,
  });

  return response.results.map((lead) => ({
    value: String(lead.id),
    label: lead.title,
  }));
}
