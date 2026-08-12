// frontend/src/components/shared/DataGrid/form/entityOption.ts

import type { EntityOption } from "./types";

export function entityOption(
  value: string | number | null | undefined,
  label: string | null | undefined,
): EntityOption | null {
  if (value == null) {
    return null;
  }

  return {
    value: String(value),
    label: label?.trim() || "Unknown",
  };
}
