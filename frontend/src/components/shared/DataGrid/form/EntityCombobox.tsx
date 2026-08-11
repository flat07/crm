// frontend/src/components/shared/DataGrid/form/EntityCombobox.tsx

import { useEffect, useRef, useState } from "react";

export interface EntityOption<
  TValue extends string | number = string | number,
> {
  value: TValue;
  label: string;
}

interface EntityComboboxProps<
  TValue extends string | number = string | number,
> {
  label?: string;

  value: TValue | null | undefined;

  selectedOption?: EntityOption<TValue> | null;

  onChange: (
    value: TValue | null,
    option?: EntityOption<TValue> | null,
  ) => void;

  searchFn: (search: string) => Promise<EntityOption<TValue>[]>;

  placeholder?: string;

  searchPlaceholder?: string;

  disabled?: boolean;

  error?: string;

  required?: boolean;

  id?: string;
}

export function EntityCombobox<
  TValue extends string | number = string | number,
>({
  label,
  value,
  selectedOption,
  onChange,
  searchFn,
  placeholder = "Select...",
  searchPlaceholder = "Search...",
  disabled = false,
  error,
  required = false,
  id,
}: EntityComboboxProps<TValue>) {
  const [open, setOpen] = useState(false);

  const [search, setSearch] = useState("");

  const [options, setOptions] = useState<EntityOption<TValue>[]>([]);

  const [loading, setLoading] = useState(false);

  const [searchError, setSearchError] = useState<string | null>(null);

  const containerRef = useRef<HTMLDivElement>(null);

  const searchTimeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  async function performSearch(query: string) {
    setLoading(true);
    setSearchError(null);

    try {
      const results = await searchFn(query);

      setOptions(results);
    } catch (error) {
      console.error("[EntityCombobox] Search failed:", error);

      setOptions([]);

      setSearchError("Unable to load results.");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    if (!open) {
      return;
    }

    if (searchTimeoutRef.current) {
      clearTimeout(searchTimeoutRef.current);
    }

    searchTimeoutRef.current = setTimeout(() => {
      void performSearch(search);
    }, 300);

    return () => {
      if (searchTimeoutRef.current) {
        clearTimeout(searchTimeoutRef.current);
      }
    };
  }, [search, open]);

  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (
        containerRef.current &&
        !containerRef.current.contains(event.target as Node)
      ) {
        setOpen(false);
      }
    }

    document.addEventListener("mousedown", handleClickOutside);

    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, []);

  function handleOpen() {
    if (disabled) {
      return;
    }

    setOpen(true);
    setSearch("");
  }

  function handleSelect(option: EntityOption<TValue>) {
    onChange(option.value, option);

    setOpen(false);
    setSearch("");
  }

  function handleClear() {
    onChange(null, null);

    setOpen(false);
    setSearch("");
    setOptions([]);
  }

  const displayOption =
    selectedOption ??
    options.find((option) => String(option.value) === String(value));

  return (
    <div ref={containerRef} className="relative space-y-1.5">
      {label && (
        <label htmlFor={id} className="text-sm font-medium">
          {label}

          {required && <span className="ml-1 text-destructive">*</span>}
        </label>
      )}

      <button
        id={id}
        type="button"
        disabled={disabled}
        onClick={handleOpen}
        className="flex h-10 w-full items-center justify-between rounded-lg border bg-background px-3 text-left text-sm outline-none focus:ring-2 focus:ring-ring disabled:cursor-not-allowed disabled:opacity-50"
      >
        <span
          className={
            displayOption ? "text-foreground" : "text-muted-foreground"
          }
        >
          {displayOption?.label ?? placeholder}
        </span>

        <span className="text-muted-foreground">▾</span>
      </button>

      {open && (
        <div className="absolute z-50 mt-1 w-full rounded-lg border bg-background shadow-lg">
          {/* Search */}
          <div className="border-b p-2">
            <input
              autoFocus
              value={search}
              onChange={(event) => setSearch(event.target.value)}
              placeholder={searchPlaceholder}
              className="h-9 w-full rounded-md border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
            />
          </div>

          {/* Results */}
          <div className="max-h-60 overflow-y-auto p-1">
            {loading && (
              <div className="px-3 py-2 text-sm text-muted-foreground">
                Searching...
              </div>
            )}

            {!loading && searchError && (
              <div className="px-3 py-2 text-sm text-destructive">
                {searchError}
              </div>
            )}

            {!loading && !searchError && options.length === 0 && (
              <div className="px-3 py-2 text-sm text-muted-foreground">
                {search ? "No results found." : "Start typing to search."}
              </div>
            )}

            {!loading &&
              !searchError &&
              options.map((option) => {
                const selected = String(option.value) === String(value);

                return (
                  <button
                    key={String(option.value)}
                    type="button"
                    onClick={() => handleSelect(option)}
                    className="flex w-full items-center rounded-md px-3 py-2 text-left text-sm hover:bg-muted"
                  >
                    <span className="flex-1">{option.label}</span>

                    {selected && <span className="text-sm">✓</span>}
                  </button>
                );
              })}

            {value != null && (
              <button
                type="button"
                onClick={handleClear}
                className="mt-1 w-full border-t px-3 py-2 text-left text-sm text-muted-foreground hover:bg-muted"
              >
                Clear selection
              </button>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
