import { useState } from "react";

interface UsePaginationOptions {
  pageSize: number;
}

export function usePagination({ pageSize }: UsePaginationOptions) {
  const [page, setPageState] = useState(1);

  function setPage(nextPage: number) {
    setPageState(Math.max(1, nextPage));
  }

  function resetPage() {
    setPageState(1);
  }

  return {
    page,
    pageSize,
    setPage,
    resetPage,
  };
}
