// frontend/src/features/deals/api/dealEntitySearch.ts
import { getDeals } from "./dealsApi";

export async function searchDeals(search: string) {
  const response = await getDeals({
    search,
    page: 1,
    page_size: 10,
  });

  return response.results.map((deal) => ({
    value: String(deal.id),
    label: String(deal.contact_name),
  }));
}
