interface GridEmptyProps {
  colSpan: number;

  message?: string;
}

export function GridEmpty({
  colSpan,
  message = "No records found.",
}: GridEmptyProps) {
  return (
    <tr>
      <td colSpan={colSpan} className="px-6 py-16 text-center">
        <div className="flex flex-col items-center gap-2">
          <div className="text-sm font-medium">{message}</div>

          <div className="text-sm text-muted-foreground">
            Try changing your search or filters.
          </div>
        </div>
      </td>
    </tr>
  );
}
