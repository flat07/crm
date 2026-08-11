// frontend/src/features/staff/types.ts

export interface Department {
  id: number;
  name: string;
  code?: string;
  description?: string;
}

export interface Role {
  id: number;
  name: string;
  code: string;
  description?: string;
}

export interface Permission {
  id: number;
  code: string;
  name: string;
  description?: string;
}

// Base staff user interface (for list view)
export interface StaffUserList {
  id: number;
  email: string;
  first_name: string;
  last_name: string;
  full_name?: string;
  department: string | null; // StringRelatedField returns the department name
  is_active: boolean;
}

// Detailed staff user interface (for detail view)
export interface StaffUserDetail extends StaffUserList {
  department_detail?: Department; // When using DepartmentSerializer
  roles: string[]; // StringRelatedField for roles
  permissions: string[]; // Permission codes
  avatar?: string | null;
  job_title?: string | null;
  phone?: string | null;
  last_login?: string; // ISO date string
  date_joined?: string; // ISO date string
  created_at?: string;
  updated_at?: string;
}

// Union type for all staff user representations
export type StaffUser = StaffUserList | StaffUserDetail;

// Staff user form data
export interface StaffFormData {
  email: string;
  first_name: string;
  last_name: string;
  phone?: string;
  department?: number | null;
  roles?: number[];
  job_title?: string;
  avatar?: File | string | null;
}

export interface CreateStaffFormData extends StaffFormData {
  password: string;
}

// Component props and state types
export interface StaffFilters {
  search?: string;
  department?: number;
  is_active?: boolean;
  ordering?: string;
}

// API Response for staff operations
export interface StaffOperationResponse {
  success: boolean;
  message: string;
  data?: StaffUserDetail | StaffUserDetail[];
}

export interface StaffListParams {
  page?: number;
  page_size?: number;
  search?: string;
  ordering?: string;
  email?: string;
  first_name?: string;
  last_name?: string;
  department?: number;
  is_active?: boolean;
}

export interface CreateStaffData {
  email: string;
  password: string;
  first_name: string;
  last_name: string;
  phone?: string;
  department?: number;
}

/**
 * Update Staff Data - matches UserUpdateSerializer
 * Excludes password field as it's not updatable through this serializer
 */
export interface UpdateStaffData {
  email?: string;
  first_name?: string;
  last_name?: string;
  phone?: string;
  department?: number | null;
  // Note: password is excluded because it's write-only in the serializer
  // and not included in UserUpdateSerializer
}
// Alternative: If you want to make all fields optional except maybe ID
export type UpdateStaffDataPartial = Partial<UpdateStaffData>;
