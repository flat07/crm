// frontend/src/components/shared/DataGrid/DataGrid.tsx
import {
  getCoreRowModel,
  useReactTable,
  type ColumnDef,
} from "@tanstack/react-table";

import { useDataGrid } from "./useDataGrid";

import { GridActions } from "./components/GridActions";
import { GridBody } from "./components/GridBody";
import { GridDrawer } from "./components/GridDrawer";
import { GridHeader } from "./components/GridHeader";
import { GridPagination } from "./components/GridPagination";
import { GridToolbar } from "./components/GridToolbar";

import type { DataGridProps } from "./types";

export function DataGrid<TData>({
  queryKey,
  queryFn,
  columns,
  pageSize = 20,
  title,
  searchPlaceholder = "Search...",
  actions,
  renderForm,
  onCreate,
  drawerTitle,
}: DataGridProps<TData>) {
  const grid = useDataGrid<TData>({
    queryKey,
    queryFn,
    pageSize,
  });
  // 🔍 LOG 1: Check what's coming from the hook
  // console.log("🔍 [DataGrid] grid.rows:", grid.rows);
  // console.log("🔍 [DataGrid] grid.total:", grid.total);
  // console.log("🔍 [DataGrid] grid.loading:", grid.loading);
  // console.log("🔍 [DataGrid] grid.error:", grid.error);

  async function handleDelete(row: TData) {
    if (!actions?.onDelete) {
      return;
    }

    await actions.onDelete(row);

    await grid.refresh();
  }

  const actionColumn = actions
    ? ({
        id: "actions",

        header: "",

        enableSorting: false,

        meta: {
          width: 60,
        },

        cell: ({ row }) => (
          <GridActions
            row={row.original}
            actions={{
              ...actions,
              onDelete: actions.onDelete ? handleDelete : undefined,
            }}
            onView={grid.drawer.openView}
            onEdit={grid.drawer.openEdit}
          />
        ),
      } satisfies ColumnDef<TData>)
    : null;

  const finalColumns = actionColumn ? [...columns, actionColumn] : columns;
  // 🔍 ADD THIS LOG - Check column accessors vs data keys
  // console.log(
  //   "🔍 [DataGrid] Column definitions with accessors:",
  //   finalColumns.map((col) => ({
  //     id: col.id,
  //     accessorKey: col.accessorKey,
  //     accessorFn: col.accessorFn ? "function" : undefined,
  //     header: typeof col.header === "string" ? col.header : "custom",
  //   })),
  // );

  // // 🔍 ADD THIS LOG - Compare with first data row
  // if (grid.rows.length > 0) {
  //   const firstRow = grid.rows[0];
  //   console.log("🔍 [DataGrid] First row data keys:", Object.keys(firstRow));
  //   console.log("🔍 [DataGrid] First row sample:", firstRow);

  //   // Check if columns match data keys
  //   const columnAccessors = finalColumns
  //     .filter((col) => col.accessorKey)
  //     .map((col) => col.accessorKey);
  //   console.log("🔍 [DataGrid] Column accessor keys:", columnAccessors);
  //   console.log("🔍 [DataGrid] Data keys:", Object.keys(firstRow));
  //   console.log(
  //     "🔍 [DataGrid] Matching keys:",
  //     columnAccessors.filter((key) => key in firstRow),
  //   );
  // }
  const table = useReactTable({
    data: grid.rows,

    columns: finalColumns,

    getCoreRowModel: getCoreRowModel(),
  });

  const columnCount = table.getVisibleLeafColumns().length;

  const errorMessage =
    grid.error instanceof Error ? grid.error.message : "Failed to load data.";

  const currentDrawerTitle =
    drawerTitle?.(grid.drawer.row, grid.drawer.mode) ??
    (grid.drawer.mode === "create"
      ? "Create"
      : grid.drawer.mode === "view"
        ? "View"
        : "Edit");

  async function handleSuccess() {
    await grid.refresh();

    grid.drawer.close();
  }

  return (
    <div className="space-y-4">
      <GridToolbar
        title={title}
        search={grid.search.value}
        searchPlaceholder={searchPlaceholder}
        loading={grid.fetching}
        onSearch={grid.search.setValue}
        onRefresh={grid.refresh}
        onCreate={onCreate ? grid.drawer.openCreate : undefined}
      />

      <div className="overflow-hidden rounded-xl border bg-background">
        <div className="overflow-x-auto">
          <table className="w-full">
            <GridHeader
              headerGroups={table.getHeaderGroups()}
              ordering={grid.ordering.value}
              onSort={grid.ordering.toggle}
            />

            <GridBody
              rows={table.getRowModel().rows}
              columnCount={columnCount}
              loading={grid.loading}
              error={grid.error ? errorMessage : undefined}
              onRetry={grid.refresh}
              onRowClick={(row) => {
                if (actions?.edit || renderForm) {
                  grid.drawer.openEdit(row);
                }
              }}
            />
          </table>
        </div>
      </div>

      <GridPagination
        page={grid.pagination.page}
        pageSize={grid.pagination.pageSize}
        total={grid.total}
        loading={grid.fetching}
        onPageChange={grid.pagination.setPage}
      />

      <GridDrawer
        open={grid.drawer.open}
        title={currentDrawerTitle}
        onClose={grid.drawer.close}
      >
        {grid.drawer.mode === "create" && onCreate?.(handleSuccess)}

        {grid.drawer.mode !== "create" &&
          renderForm?.(grid.drawer.row, grid.drawer.mode, handleSuccess)}
      </GridDrawer>
    </div>
  );
}
