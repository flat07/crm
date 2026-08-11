// frontend/src/features/staff/api/staffEntitySearch.ts
import { getStaff } from "./staffApi";

export async function searchStaff(search: string) {
  const response = await getStaff({
    search,
    page: 1,
    page_size: 10,
  });

  return response.results.map((staff) => ({
    value: String(staff.id), // Convert to string
    label: staff.full_name ?? staff.email,
  }));
}
