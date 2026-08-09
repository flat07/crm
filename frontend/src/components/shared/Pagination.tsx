import { Button } from "@/components/ui/button";

interface Props {
  page: number;
  hasNext: boolean;
  hasPrevious: boolean;
  onNext: () => void;
  onPrevious: () => void;
}

export function Pagination({
  page,
  hasNext,
  hasPrevious,
  onNext,
  onPrevious,
}: Props) {
  return (
    <div className="flex items-center justify-end gap-2">
      <Button variant="outline" disabled={!hasPrevious} onClick={onPrevious}>
        Previous
      </Button>

      <span>{page}</span>

      <Button disabled={!hasNext} onClick={onNext}>
        Next
      </Button>
    </div>
  );
}
