// frontend/src/features/activities/types.ts

export interface ActivityQueryParams {
  page?: number;
  page_size?: number;
  search?: string;
  ordering?: string;
  activity_type?: string;
  status?: string;
  priority?: string;
  owner?: string;
  created_by?: string;
  content_type?: string;
  object_id?: string;
  is_active?: boolean;
}

export interface Activity {
  id: string;

  title: string;
  description: string;

  activity_type: ActivityType;
  status: ActivityStatus;
  priority: ActivityPriority;

  due_date: string | null;
  completed_at: string | null;

  owner: ActivityUser | null;
  owner_name: string | null;
  created_by: ActivityUser | null;

  content_type: string;
  content_type_name: string | null;
  object_id: string;
  content_object_name: string | null;

  created_at: string;
  updated_at: string;
}

export interface ActivityUser {
  id: string;
  first_name: string | null;
  last_name: string | null;
  full_name?: string | null;
}

export interface ActivityFormData {
  title: string;
  description?: string;

  activity_type: ActivityType;
  status?: ActivityStatus;
  priority?: ActivityPriority;

  due_date?: string | null;
  completed_at?: string | null;

  owner_id?: string | null;

  content_type: "company" | "contact" | "lead" | "deal";
  object_id: string;
}

export enum ActivityType {
  CALL = "call",
  EMAIL = "email",
  MEETING = "meeting",
  TASK = "task",
  NOTE = "note",
}

export enum ActivityStatus {
  PLANNED = "planned",
  IN_PROGRESS = "in_progress",
  COMPLETED = "completed",
  CANCELLED = "cancelled",
}

export enum ActivityPriority {
  LOW = "low",
  MEDIUM = "medium",
  HIGH = "high",
  URGENT = "urgent",
}
