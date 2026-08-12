// frontend/src/components/shared/DataGrid/column.ts
import type { ColumnDef } from "@tanstack/react-table";

interface ColumnOptions<TData> {
  accessorKey: keyof TData;
  header: string;
  sortable?: boolean;
  width?: number | string;
  cell?: ColumnDef<TData>["cell"];
}

export function column<TData>({
  accessorKey,
  header,
  sortable = true,
  width,
  cell,
}: ColumnOptions<TData>): ColumnDef<TData> {
  return {
    id: accessorKey as string, // Add explicit id
    accessorKey: accessorKey as string,
    header,
    // 🔥 FIX: Provide default cell renderer if none is given
    cell:
      cell ??
      (({ row }) => {
        const value = row.getValue(accessorKey as string);

        if (value == null) {
          return "";
        }

        if (typeof value === "boolean") {
          return value ? "Yes" : "No";
        }

        return String(value);
      }),
    enableSorting: sortable,
    meta: {
      sortable,
      orderingField: accessorKey as string,
      width,
    },
  };
}
