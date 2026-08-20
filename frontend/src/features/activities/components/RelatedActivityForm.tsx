import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";

import { useCreateActivity } from "../hooks/useCreateActivity";
import type { ActivityFormData } from "../types";

const relatedActivitySchema = z.object({
  title: z.string().min(1, "Title is required"),
  description: z.string().optional(),
  activity_type: z.string().min(1, "Activity type is required"),
  status: z.string().min(1, "Status is required"),
  priority: z.string().min(1, "Priority is required"),
  due_date: z.string().optional(),
});

type RelatedActivityFormValues = z.infer<typeof relatedActivitySchema>;

type ContentType = "company" | "contact" | "lead" | "deal";

interface RelatedActivityFormProps {
  contentType: ContentType;
  objectId: string;
  onSuccess?: () => void;
  onCancel?: () => void;
}

export function RelatedActivityForm({
  contentType,
  objectId,
  onSuccess,
  onCancel,
}: RelatedActivityFormProps) {
  const createActivity = useCreateActivity();

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<RelatedActivityFormValues>({
    resolver: zodResolver(relatedActivitySchema),

    defaultValues: {
      title: "",
      description: "",
      activity_type: "task",
      status: "planned",
      priority: "medium",
      due_date: "",
    },
  });

  async function handleFormSubmit(values: RelatedActivityFormValues) {
    const payload: ActivityFormData = {
      ...values,
      due_date: values.due_date || undefined,
      content_type: contentType,
      object_id: objectId,
    };

    await createActivity.mutateAsync(payload);

    reset();

    onSuccess?.();
  }

  return (
    <div className="space-y-4">
      {/* Title */}
      <div className="space-y-2">
        <label htmlFor="activity-title" className="text-sm font-medium">
          Title
        </label>

        <Input
          id="activity-title"
          {...register("title")}
          placeholder="Call with customer"
        />

        {errors.title && (
          <p className="text-sm text-destructive">{errors.title.message}</p>
        )}
      </div>

      {/* Activity type */}
      <div className="space-y-2">
        <label htmlFor="activity-type" className="text-sm font-medium">
          Activity type
        </label>

        <select
          id="activity-type"
          {...register("activity_type")}
          className="border-input bg-background w-full rounded-md border px-3 py-2 text-sm"
        >
          <option value="call">Call</option>
          <option value="email">Email</option>
          <option value="meeting">Meeting</option>
          <option value="task">Task</option>
          <option value="note">Note</option>
        </select>

        {errors.activity_type && (
          <p className="text-sm text-destructive">
            {errors.activity_type.message}
          </p>
        )}
      </div>

      {/* Status */}
      <div className="space-y-2">
        <label htmlFor="activity-status" className="text-sm font-medium">
          Status
        </label>

        <select
          id="activity-status"
          {...register("status")}
          className="border-input bg-background w-full rounded-md border px-3 py-2 text-sm"
        >
          <option value="planned">Planned</option>
          <option value="in_progress">In progress</option>
          <option value="completed">Completed</option>
        </select>

        {errors.status && (
          <p className="text-sm text-destructive">{errors.status.message}</p>
        )}
      </div>

      {/* Priority */}
      <div className="space-y-2">
        <label htmlFor="activity-priority" className="text-sm font-medium">
          Priority
        </label>

        <select
          id="activity-priority"
          {...register("priority")}
          className="border-input bg-background w-full rounded-md border px-3 py-2 text-sm"
        >
          <option value="low">Low</option>
          <option value="medium">Medium</option>
          <option value="high">High</option>
          <option value="urgent">Urgent</option>
        </select>

        {errors.priority && (
          <p className="text-sm text-destructive">{errors.priority.message}</p>
        )}
      </div>

      {/* Due date */}
      <div className="space-y-2">
        <label htmlFor="activity-due-date" className="text-sm font-medium">
          Due date
        </label>

        <Input
          id="activity-due-date"
          type="datetime-local"
          {...register("due_date")}
        />

        {errors.due_date && (
          <p className="text-sm text-destructive">{errors.due_date.message}</p>
        )}
      </div>

      {/* Description */}
      <div className="space-y-2">
        <label htmlFor="activity-description" className="text-sm font-medium">
          Description
        </label>

        <Textarea
          id="activity-description"
          {...register("description")}
          placeholder="Add some details..."
          rows={4}
        />

        {errors.description && (
          <p className="text-sm text-destructive">
            {errors.description.message}
          </p>
        )}
      </div>

      {/* Actions */}
      <div className="flex justify-end gap-2">
        {onCancel && (
          <Button
            type="button"
            variant="outline"
            onClick={onCancel}
            disabled={isSubmitting || createActivity.isPending}
          >
            Cancel
          </Button>
        )}

        <Button
          type="button"
          disabled={isSubmitting || createActivity.isPending}
          onClick={handleSubmit(handleFormSubmit)}
        >
          {isSubmitting || createActivity.isPending
            ? "Creating..."
            : "Add activity"}
        </Button>
      </div>
    </div>
  );
}
