// frontend/src/components/shared/FormError.tsx

interface Props {
  message?: string;
}

export default function FormError({ message }: Props) {
  if (!message) return null;

  return <p className="text-sm font-medium text-destructive">{message}</p>;
}
