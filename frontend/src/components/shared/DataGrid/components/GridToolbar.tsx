import { Plus, RefreshCw, Search, X } from "lucide-react";

interface GridToolbarProps {
  title?: string;

  search: string;

  searchPlaceholder?: string;

  loading?: boolean;

  onSearch(value: string): void;

  onRefresh(): void;

  onCreate?(): void;
}

export function GridToolbar({
  title,
  search,
  searchPlaceholder = "Search...",
  loading = false,
  onSearch,
  onRefresh,
  onCreate,
}: GridToolbarProps) {
  return (
    <div className="flex min-h-10 items-center justify-between gap-4">
      {/* Left */}
      <div className="min-w-0 flex-1">
        {title && <h2 className="truncate text-lg font-semibold">{title}</h2>}
      </div>

      {/* Center */}
      <div className="relative w-full max-w-md">
        <Search className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />

        <input
          type="text"
          value={search}
          onChange={(event) => onSearch(event.target.value)}
          placeholder={searchPlaceholder}
          className="h-10 w-full rounded-lg border bg-background pl-9 pr-9 text-sm outline-none transition focus:ring-2 focus:ring-ring"
        />

        {search && (
          <button
            type="button"
            onClick={() => onSearch("")}
            className="absolute right-2 top-1/2 flex h-7 w-7 -translate-y-1/2 items-center justify-center rounded-md text-muted-foreground hover:bg-muted hover:text-foreground"
            aria-label="Clear search"
          >
            <X className="h-4 w-4" />
          </button>
        )}
      </div>

      {/* Right */}
      <div className="flex min-w-0 flex-1 justify-end gap-2">
        <button
          type="button"
          onClick={onRefresh}
          disabled={loading}
          className="inline-flex h-10 items-center justify-center gap-2 rounded-lg border px-3 text-sm font-medium transition hover:bg-muted disabled:pointer-events-none disabled:opacity-50"
          aria-label="Refresh"
        >
          <RefreshCw className={`h-4 w-4 ${loading ? "animate-spin" : ""}`} />

          <span className="hidden sm:inline">Refresh</span>
        </button>

        {onCreate && (
          <button
            type="button"
            onClick={onCreate}
            className="inline-flex h-10 items-center justify-center gap-2 rounded-lg bg-primary px-4 text-sm font-medium text-primary-foreground transition hover:bg-primary/90"
          >
            <Plus className="h-4 w-4" />

            <span>New</span>
          </button>
        )}
      </div>
    </div>
  );
}
