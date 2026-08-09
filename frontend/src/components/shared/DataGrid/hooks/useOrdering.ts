import { useState } from "react";

export function useOrdering() {
  const [value, setValue] = useState("");

  function toggle(field: string) {
    if (value === field) {
      setValue(`-${field}`);
      return;
    }

    if (value === `-${field}`) {
      setValue("");
      return;
    }

    setValue(field);
  }

  function clear() {
    setValue("");
  }

  return {
    value,
    toggle,
    clear,
  };
}
