import { useState } from "react";

export function useTable() {
  const [page, setPage] = useState(1);

  const [pageSize] = useState(20);

  const [search, setSearch] = useState("");

  const [ordering, setOrdering] = useState("");

  return {
    page,
    pageSize,
    search,
    ordering,

    setPage,
    setSearch,
    setOrdering,
  };
}
