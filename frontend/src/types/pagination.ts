export interface PaginationParams {
  page?: number;

  page_size?: number;

  search?: string;

  ordering?: string;
}

export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}
