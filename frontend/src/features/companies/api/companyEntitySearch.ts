// frontend/src/features/companies/api/companyEntitySearch.ts
import { getCompanies } from "./companyApi";

export async function searchCompanies(search: string) {
  const response = await getCompanies({
    search,
    page: 1,
    page_size: 10,
  });

  return response.results.map((company) => ({
    value: String(company.id),
    label: company.name,
  }));
}
