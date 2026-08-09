export function totalPages(count: number, pageSize: number) {
  return Math.ceil(count / pageSize);
}
