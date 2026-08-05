// frontend/src/components/shared/PageTitle.tsx

interface Props {
  title: string;
  description?: string;
}

export default function PageTitle({ title, description }: Props) {
  return (
    <div className="space-y-1">
      <h2 className="text-2xl font-bold">{title}</h2>

      {description && <p className="text-muted-foreground">{description}</p>}
    </div>
  );
}
