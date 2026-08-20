// frontend/src/features/leads/hooks/useLeads.ts
import { useQuery } from "@tanstack/react-query";
import type { LeadListParams } from "../api/leadsApi";
import { getLead, getLeads } from "../api/leadsApi";

export const LEADS_QUERY_KEY = "leads";

/**
 * Hook to fetch a paginated list of leads with filters.
 */
export function useLeads(params: LeadListParams = {}) {
  return useQuery({
    queryKey: [LEADS_QUERY_KEY, params],
    queryFn: () => getLeads(params),
    staleTime: 5 * 60 * 1000, // 5 minutes
  });
}

/**
 * Hook to fetch a single lead by ID.
 */
export function useLead(id: string) {
  return useQuery({
    queryKey: [LEADS_QUERY_KEY, id],
    queryFn: () => getLead(id),
    enabled: !!id,
    staleTime: 5 * 60 * 1000,
  });
}
