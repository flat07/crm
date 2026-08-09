export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}
export interface TableQuery {
  page: number;
  pageSize: number;
  search: string;
  ordering: string;
}
export interface TableResponse<T> {
  rows: T[];
  total: number;
}
