// frontend/src/components/shared/EmptyState.tsx

interface Props {
  title: string;
  description: string;
}

export default function EmptyState({ title, description }: Props) {
  return (
    <div className="rounded-lg border border-dashed p-8 text-center">
      <h3 className="font-semibold">{title}</h3>

      <p className="mt-2 text-sm text-muted-foreground">{description}</p>
    </div>
  );
}
