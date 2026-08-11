// frontend/src/components/shared/DataGrid/form/EntitySelect.tsx
export interface EntityOption<
  TValue extends string | number = string | number,
> {
  value: TValue;
  label: string;
}

interface EntitySelectProps<TValue extends string | number = string | number> {
  label?: string;
  value: TValue | null | undefined;
  options: EntityOption<TValue>[];
  onChange: (value: TValue | null) => void;
  placeholder?: string;
  disabled?: boolean;
  error?: string;
  required?: boolean;
  id?: string;
}

export function EntitySelect<TValue extends string | number = string | number>({
  label,
  value,
  options,
  onChange,
  placeholder = "Select...",
  disabled = false,
  error,
  required = false,
  id,
}: EntitySelectProps<TValue>) {
  return (
    <div className="space-y-1.5">
      {label && (
        <label htmlFor={id} className="text-sm font-medium">
          {label}

          {required && <span className="ml-1 text-destructive">*</span>}
        </label>
      )}

      <select
        id={id}
        value={value ?? ""}
        disabled={disabled}
        onChange={(event) => {
          const selectedValue = event.target.value;

          if (selectedValue === "") {
            onChange(null);
            return;
          }

          const option = options.find(
            (option) => String(option.value) === selectedValue,
          );

          onChange(option?.value ?? null);
        }}
        className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring disabled:cursor-not-allowed disabled:opacity-50"
      >
        <option value="">{placeholder}</option>

        {options.map((option) => (
          <option key={String(option.value)} value={String(option.value)}>
            {option.label}
          </option>
        ))}
      </select>

      {error && <p className="text-sm text-destructive">{error}</p>}
    </div>
  );
}
