// frontend/src/components/shared/DataGrid/useDataGrid.ts
import { useMemo } from "react";

import { QueryKey, useQuery, useQueryClient } from "@tanstack/react-query";

import { useDrawer } from "./hooks/useDrawer";
import { useOrdering } from "./hooks/useOrdering";
import { usePagination } from "./hooks/usePagination";
import { useSearch } from "./hooks/useSearch";

import type { GridQueryParams, PaginatedResponse } from "./types";

interface UseDataGridOptions<TData> {
  queryKey: QueryKey;

  queryFn(params: GridQueryParams): Promise<PaginatedResponse<TData>>;

  pageSize: number;
}

export function useDataGrid<TData>({
  queryKey,
  queryFn,
  pageSize,
}: UseDataGridOptions<TData>) {
  const queryClient = useQueryClient();

  const search = useSearch();

  const pagination = usePagination({
    pageSize,
  });

  const ordering = useOrdering();

  const drawer = useDrawer<TData>();

  const params = useMemo(
    () => ({
      page: pagination.page,

      page_size: pagination.pageSize,

      search: search.debounced,

      ordering: ordering.value,
    }),
    [pagination.page, pagination.pageSize, search.debounced, ordering.value],
  );

  const query = useQuery({
    queryKey: [...queryKey, params],

    queryFn: () => queryFn(params),

    placeholderData: (previous) => previous,
  });
  // 🔍 LOG 8: Check query results
  // console.log("🔍 [useDataGrid] Query status:", {
  //   isPending: query.isPending,
  //   isFetching: query.isFetching,
  //   isError: query.isError,
  //   error: query.error,
  //   data: query.data,
  //   results: query.data?.results,
  //   count: query.data?.count,
  // });

  // // 🔍 LOG 9: Check raw data structure
  // if (query.data?.results?.length > 0) {
  //   console.log("🔍 [useDataGrid] First result sample:", query.data.results[0]);
  //   console.log(
  //     "🔍 [useDataGrid] Result keys:",
  //     Object.keys(query.data.results[0]),
  //   );
  // }

  function handleSearch(value: string) {
    search.setValue(value);

    pagination.resetPage();
  }

  function handleOrdering(field: string) {
    ordering.toggle(field);

    pagination.resetPage();
  }

  async function refresh() {
    await queryClient.invalidateQueries({
      queryKey,
    });
  }

  return {
    query,

    rows: query.data?.results ?? [],

    total: query.data?.count ?? 0,

    loading: query.isPending,

    fetching: query.isFetching,

    error: query.error,

    search: {
      value: search.value,

      debounced: search.debounced,

      setValue: handleSearch,

      clear: search.clear,
    },

    pagination,

    ordering: {
      value: ordering.value,

      toggle: handleOrdering,

      clear: ordering.clear,
    },

    drawer,

    refresh,
  };
}
