import { z } from "zod";

// -----------------------------------------------------------------------------
// Activity choices
// -----------------------------------------------------------------------------

export const activityTypeValues = [
  "call",
  "email",
  "meeting",
  "task",
  "note",
] as const;

export const activityStatusValues = [
  "planned",
  "in_progress",
  "completed",
  "cancelled",
] as const;

export const activityPriorityValues = [
  "low",
  "medium",
  "high",
  "urgent",
] as const;

// -----------------------------------------------------------------------------
// Labels for UI
// -----------------------------------------------------------------------------

export const activityTypeOptions = [
  { value: "call", label: "Call" },
  { value: "email", label: "Email" },
  { value: "meeting", label: "Meeting" },
  { value: "task", label: "Task" },
  { value: "note", label: "Note" },
] as const;

export const activityStatusOptions = [
  { value: "planned", label: "Planned" },
  { value: "in_progress", label: "In Progress" },
  { value: "completed", label: "Completed" },
  { value: "cancelled", label: "Cancelled" },
] as const;

export const activityPriorityOptions = [
  { value: "low", label: "Low" },
  { value: "medium", label: "Medium" },
  { value: "high", label: "High" },
  { value: "urgent", label: "Urgent" },
] as const;

// -----------------------------------------------------------------------------
// Schema
// -----------------------------------------------------------------------------

export const activityFormSchema = z.object({
  title: z.string().min(1, "Title is required").max(255),

  description: z.string().optional().or(z.literal("")),

  activity_type: z.enum(activityTypeValues),

  status: z.enum(activityStatusValues).default("planned"),

  priority: z.enum(activityPriorityValues).default("medium"),

  due_date: z.string().optional().or(z.literal("")),

  completed_at: z.string().optional().or(z.literal("")),

  owner_id: z.uuid("Invalid owner ID").nullable().optional(),

  content_type: z.string().min(1, "Related object type is required"),

  object_id: z.string().uuid("Invalid object ID"),
});

// -----------------------------------------------------------------------------
// Types
// -----------------------------------------------------------------------------

export type ActivityFormInput = z.input<typeof activityFormSchema>;

export type ActivityFormValues = z.output<typeof activityFormSchema>;
