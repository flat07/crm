interface GridLoadingProps {
  colSpan: number;

  rows?: number;
}

export function GridLoading({ colSpan, rows = 6 }: GridLoadingProps) {
  return (
    <>
      {Array.from({ length: rows }).map((_, index) => (
        <tr key={index}>
          {Array.from({
            length: colSpan,
          }).map((_, cellIndex) => (
            <td key={cellIndex} className="px-4 py-3">
              <div className="h-4 w-full animate-pulse rounded bg-muted" />
            </td>
          ))}
        </tr>
      ))}
    </>
  );
}
