import { Input } from "@/components/ui/input";

interface Props {
  value: string;
  onChange(value: string): void;
}

export function SearchInput({ value, onChange }: Props) {
  return (
    <Input
      placeholder="Search..."
      value={value}
      onChange={(e) => onChange(e.target.value)}
    />
  );
}
