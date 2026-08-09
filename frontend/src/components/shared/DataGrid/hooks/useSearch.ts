import { useState } from "react";

import { useDebounce } from "./useDebounce";

export function useSearch() {
  const [value, setValue] = useState("");

  const debounced = useDebounce(value);

  return {
    value,

    debounced,

    setValue,

    clear() {
      setValue("");
    },
  };
}
