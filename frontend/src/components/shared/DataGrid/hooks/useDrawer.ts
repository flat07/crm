import { useState } from "react";

export type DrawerMode = "create" | "view" | "edit";

export function useDrawer<TData>() {
  const [open, setOpen] = useState(false);

  const [row, setRow] = useState<TData | null>(null);

  const [mode, setMode] = useState<DrawerMode>("create");

  function openCreate() {
    setRow(null);
    setMode("create");
    setOpen(true);
  }

  function openView(row: TData) {
    setRow(row);
    setMode("view");
    setOpen(true);
  }

  function openEdit(row: TData) {
    setRow(row);
    setMode("edit");
    setOpen(true);
  }

  function close() {
    setOpen(false);
    setRow(null);
    setMode("create");
  }

  return {
    open,
    row,
    mode,

    openCreate,
    openView,
    openEdit,

    close,
  };
}
