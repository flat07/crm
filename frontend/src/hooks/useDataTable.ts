import { useMemo, useState } from "react";

import { QueryKey, useQuery } from "@tanstack/react-query";

interface ApiResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}

interface UseDataTableProps<T> {
  queryKey: QueryKey;

  queryFn(params: {
    page: number;
    page_size: number;
    search: string;
    ordering: string;
  }): Promise<ApiResponse<T>>;

  initialPageSize?: number;
}

export function useDataTable<T>({
  queryKey,
  queryFn,
  initialPageSize = 20,
}: UseDataTableProps<T>) {
  const [page, setPage] = useState(1);

  const [pageSize] = useState(initialPageSize);

  const [search, setSearch] = useState("");

  const [ordering, setOrdering] = useState("");

  const params = useMemo(
    () => ({
      page,
      page_size: pageSize,
      search,
      ordering,
    }),
    [page, pageSize, search, ordering],
  );

  const query = useQuery({
    queryKey: [...queryKey, params],

    queryFn: () => queryFn(params),

    placeholderData: (previous) => previous,
  });

  return {
    rows: query.data?.results ?? [],

    total: query.data?.count ?? 0,

    loading: query.isPending,

    error: query.error?.message,

    page,

    pageSize,

    search,

    ordering,

    setPage,

    setSearch,

    setOrdering,

    refetch: query.refetch,
  };
}
