// frontend/src/components/shared/DataGrid/components/GridBody.tsx
import { flexRender, type Row } from "@tanstack/react-table";

import { GridEmpty } from "./GridEmpty";
import { GridError } from "./GridError";
import { GridLoading } from "./GridLoading";

interface GridBodyProps<TData> {
  rows: Row<TData>[];

  columnCount: number;

  loading: boolean;

  error?: string;

  onRetry(): void;

  onRowClick(row: TData): void;
}

export function GridBody<TData>({
  rows,
  columnCount,
  loading,
  error,
  onRetry,
  onRowClick,
}: GridBodyProps<TData>) {
  // 🔍 LOG 4: Check what GridBody receives
  // console.log("🔍 [GridBody] rows received:", rows);
  // console.log("🔍 [GridBody] rows length:", rows.length);
  // console.log("🔍 [GridBody] columnCount:", columnCount);

  if (loading) {
    return (
      <tbody>
        <GridLoading colSpan={columnCount} />
      </tbody>
    );
  }

  if (error) {
    return (
      <tbody>
        <GridError colSpan={columnCount} message={error} onRetry={onRetry} />
      </tbody>
    );
  }

  if (rows.length === 0) {
    return (
      <tbody>
        <GridEmpty colSpan={columnCount} />
      </tbody>
    );
  }

  return (
    <tbody>
      {rows.map((row) => (
        <tr
          key={row.id}
          onClick={() => onRowClick(row.original)}
          className="cursor-pointer border-b transition-colors last:border-b-0 hover:bg-muted/40"
        >
          {row.getVisibleCells().map((cell) => (
            <td key={cell.id} className="px-4 py-3 text-sm">
              {flexRender(cell.column.columnDef.cell, cell.getContext())}
            </td>
          ))}
        </tr>
      ))}
    </tbody>
  );
}
