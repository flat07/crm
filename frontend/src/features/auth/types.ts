// frontend/src/features/auth/types.ts

export interface LoginRequest {
  email: string;
  password: string;
}

export interface Department {
  id: string;
  name: string;
}

export interface User {
  id: string;
  email: string;
  first_name: string;
  last_name: string;
  department: Department | null;
  roles: string[];
  avatar: string | null;
  job_title: string;
  permissions: string[];
}

export interface LoginResponse {
  access: string;
  refresh: string;
  user: User;
}
