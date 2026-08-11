import { getContacts } from "./contactApi";

export async function searchContacts(search: string) {
  const response = await getContacts({
    search,
    page: 1,
    page_size: 10,
  });

  return response.results.map((contact) => ({
    value: String(contact.id),
    label: contact.full_name,
  }));
}
