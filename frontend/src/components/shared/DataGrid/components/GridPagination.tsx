import { ChevronLeft, ChevronRight } from "lucide-react";

interface GridPaginationProps {
  page: number;

  pageSize: number;

  total: number;

  loading?: boolean;

  onPageChange(page: number): void;
}

export function GridPagination({
  page,
  pageSize,
  total,
  loading = false,
  onPageChange,
}: GridPaginationProps) {
  const totalPages = Math.max(1, Math.ceil(total / pageSize));

  const hasPrevious = page > 1;

  const hasNext = page < totalPages;

  const firstItem = total === 0 ? 0 : (page - 1) * pageSize + 1;

  const lastItem = Math.min(page * pageSize, total);

  return (
    <div className="flex items-center justify-between border-t pt-4">
      {/* Results */}
      <div className="text-sm text-muted-foreground">
        {total === 0 ? (
          "No results"
        ) : (
          <>
            Showing{" "}
            <span className="font-medium text-foreground">{firstItem}</span> to{" "}
            <span className="font-medium text-foreground">{lastItem}</span> of{" "}
            <span className="font-medium text-foreground">{total}</span>
          </>
        )}
      </div>

      {/* Controls */}
      <div className="flex items-center gap-2">
        <button
          type="button"
          disabled={loading || !hasPrevious}
          onClick={() => onPageChange(page - 1)}
          className="inline-flex h-9 w-9 items-center justify-center rounded-md border transition hover:bg-muted disabled:pointer-events-none disabled:opacity-40"
          aria-label="Previous page"
        >
          <ChevronLeft className="h-4 w-4" />
        </button>

        <div className="min-w-20 text-center text-sm">
          Page <span className="font-medium">{page}</span> of{" "}
          <span className="font-medium">{totalPages}</span>
        </div>

        <button
          type="button"
          disabled={loading || !hasNext}
          onClick={() => onPageChange(page + 1)}
          className="inline-flex h-9 w-9 items-center justify-center rounded-md border transition hover:bg-muted disabled:pointer-events-none disabled:opacity-40"
          aria-label="Next page"
        >
          <ChevronRight className="h-4 w-4" />
        </button>
      </div>
    </div>
  );
}
