import { AlertCircle, RefreshCw } from "lucide-react";

interface GridErrorProps {
  colSpan: number;

  message?: string;

  onRetry(): void;
}

export function GridError({
  colSpan,
  message = "Failed to load data.",
  onRetry,
}: GridErrorProps) {
  return (
    <tr>
      <td colSpan={colSpan} className="px-6 py-16 text-center">
        <div className="flex flex-col items-center gap-3">
          <AlertCircle className="h-6 w-6 text-destructive" />

          <div className="text-sm font-medium">{message}</div>

          <button
            type="button"
            onClick={onRetry}
            className="inline-flex items-center gap-2 rounded-lg border px-3 py-2 text-sm font-medium hover:bg-muted"
          >
            <RefreshCw className="h-4 w-4" />
            Try again
          </button>
        </div>
      </td>
    </tr>
  );
}
