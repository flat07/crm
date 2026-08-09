import { flexRender, type HeaderGroup } from "@tanstack/react-table";

import { ArrowDown, ArrowUp, ArrowUpDown } from "lucide-react";

interface GridHeaderProps<TData> {
  headerGroups: HeaderGroup<TData>[];

  ordering: string;

  onSort(field: string): void;
}

export function GridHeader<TData>({
  headerGroups,
  ordering,
  onSort,
}: GridHeaderProps<TData>) {
  return (
    <thead className="bg-muted/50">
      {headerGroups.map((headerGroup) => (
        <tr key={headerGroup.id}>
          {headerGroup.headers.map((header) => {
            const meta = header.column.columnDef.meta;

            const sortable = meta?.sortable === true;

            const orderingField = meta?.orderingField;

            const isAsc = orderingField && ordering === orderingField;

            const isDesc = orderingField && ordering === `-${orderingField}`;

            return (
              <th
                key={header.id}
                style={{
                  width: meta?.width,
                }}
                className="border-b px-4 py-3 text-left text-sm font-semibold"
              >
                {sortable && orderingField ? (
                  <button
                    type="button"
                    onClick={() => onSort(orderingField)}
                    className="group inline-flex items-center gap-2 rounded-md outline-none transition hover:text-primary focus-visible:ring-2 focus-visible:ring-ring"
                  >
                    <span>
                      {flexRender(
                        header.column.columnDef.header,
                        header.getContext(),
                      )}
                    </span>

                    {isAsc && <ArrowUp className="h-4 w-4" />}

                    {isDesc && <ArrowDown className="h-4 w-4" />}

                    {!isAsc && !isDesc && (
                      <ArrowUpDown className="h-4 w-4 text-muted-foreground transition group-hover:text-foreground" />
                    )}
                  </button>
                ) : (
                  flexRender(
                    header.column.columnDef.header,
                    header.getContext(),
                  )
                )}
              </th>
            );
          })}
        </tr>
      ))}
    </thead>
  );
}
