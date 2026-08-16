// frontend/src/features/notes/components/NotesToolbar.tsx

import { Plus, Search } from "lucide-react";

interface NotesToolbarProps {
  search: string;
  onSearchChange: (value: string) => void;
  onAdd: () => void;
}

export function NotesToolbar({
  search,
  onSearchChange,
  onAdd,
}: NotesToolbarProps) {
  return (
    <div className="flex items-center justify-between gap-4">
      <div className="relative max-w-md flex-1">
        <Search className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />

        <input
          value={search}
          onChange={(event) => onSearchChange(event.target.value)}
          placeholder="Search notes..."
          className="h-10 w-full rounded-lg border bg-background pl-9 pr-3 text-sm outline-none focus:ring-2 focus:ring-ring"
        />
      </div>

      <button
        type="button"
        onClick={onAdd}
        className="inline-flex h-10 items-center gap-2 rounded-lg bg-primary px-4 text-sm font-medium text-primary-foreground hover:bg-primary/90"
      >
        <Plus className="h-4 w-4" />
        Add Note
      </button>
    </div>
  );
}
