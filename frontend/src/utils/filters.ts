export function removeEmptyFilters<T extends object>(filters: T) {
  return Object.fromEntries(
    Object.entries(filters).filter(
      ([_, value]) => value !== "" && value !== null && value !== undefined,
    ),
  );
}
