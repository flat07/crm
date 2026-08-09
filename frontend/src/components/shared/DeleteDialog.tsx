import { Button } from "@/components/ui/button";
interface Props {
  open: boolean;

  onClose(): void;

  onConfirm(): void;
}

export function DeleteDialog({
  open,

  onClose,

  onConfirm,
}: Props) {
  if (!open) return null;

  return (
    <div>
      <h2>Delete this record?</h2>

      <Button variant="outline" onClick={onClose}>
        Cancel
      </Button>

      <Button
        variant="destructive"

        onClick={onConfirm}
      >
        Delete
      </Button>
    </div>
  );
}
