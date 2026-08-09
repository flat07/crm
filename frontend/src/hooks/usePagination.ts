import { useState } from "react";

export function usePagination() {
  const [page, setPage] = useState(1);

  const nextPage = () => setPage((p) => p + 1);

  const prevPage = () => setPage((p) => Math.max(1, p - 1));

  return {
    page,

    setPage,

    nextPage,

    prevPage,
  };
}
