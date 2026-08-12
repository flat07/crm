// frontend/src/components/shared/DataGrid/types.ts
import type { QueryKey } from "@tanstack/react-query";
import type { ColumnDef, RowData } from "@tanstack/react-table";
import type { DrawerMode } from "./hooks/useDrawer";

export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}

export interface GridQueryParams {
  page: number;
  page_size: number;
  search: string;
  ordering: string;
}

export interface DataGridActions<TData> {
  view?: boolean;
  edit?: boolean;
  delete?: boolean;

  onView?: (row: TData) => void;
  onEdit?: (row: TData) => void;
  onDelete?: (row: TData) => Promise<void>;
}

export interface DataGridProps<TData> {
  queryKey: QueryKey;

  queryFn(params: GridQueryParams): Promise<PaginatedResponse<TData>>;

  columns: ColumnDef<TData>[];

  pageSize?: number;

  title?: string;

  searchPlaceholder?: string;

  actions?: DataGridActions<TData>;

  renderForm?(
    row: TData | null,
    mode: DrawerMode,
    onSuccess: () => Promise<void>,
  ): React.ReactNode;

  onCreate?(onSuccess: () => Promise<void>): React.ReactNode;

  drawerTitle?(row: TData | null, mode: DrawerMode): string;
}

declare module "@tanstack/react-table" {
  interface ColumnMeta<TData extends RowData, TValue> {
    sortable?: boolean;
    orderingField?: string;
    width?: number | string;
    className?: string;
    isNumeric?: boolean;
  }
}
