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
        // Return the value or empty string if null/undefined
        return value ?? "";
      }),
    enableSorting: false,
    meta: {
      sortable,
      orderingField: accessorKey as string,
      width,
    },
  };
}
