import { X } from "lucide-react";

interface GridDrawerProps {
  open: boolean;

  title?: string;

  children: React.ReactNode;

  onClose(): void;
}

export function GridDrawer({
  open,
  title = "Details",
  children,
  onClose,
}: GridDrawerProps) {
  if (!open) {
    return null;
  }

  return (
    <div className="fixed inset-0 z-50">
      {/* Overlay */}
      <button
        type="button"
        aria-label="Close drawer"
        onClick={onClose}
        className="absolute inset-0 bg-black/30"
      />

      {/* Drawer */}
      <aside className="absolute right-0 top-0 flex h-full w-full max-w-xl flex-col border-l bg-background shadow-xl">
        {/* Header */}
        <div className="flex h-16 shrink-0 items-center justify-between border-b px-6">
          <h2 className="text-lg font-semibold">{title}</h2>

          <button
            type="button"
            onClick={onClose}
            className="inline-flex h-9 w-9 items-center justify-center rounded-md hover:bg-muted"
            aria-label="Close"
          >
            <X className="h-5 w-5" />
          </button>
        </div>

        {/* Content */}
        <div className="flex-1 overflow-y-auto p-6">{children}</div>
      </aside>
    </div>
  );
}
