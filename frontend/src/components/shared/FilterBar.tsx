interface Props {
  children: React.ReactNode;
}

export function FilterBar({ children }: Props) {
  return (
    <div className="mb-5 flex items-center justify-between gap-4">
      {children}
    </div>
  );
}
