import { zodResolver } from "@hookform/resolvers/zod";
import { useEffect } from "react";
import { Controller, useForm, useWatch } from "react-hook-form";

import { EntityCombobox } from "@/components/shared/DataGrid/form";
import { entityOption } from "@/components/shared/DataGrid/form/entityOption";

import { searchCompanies } from "@/features/companies/api/companyEntitySearch";
import { searchContacts } from "@/features/contacts/api/contactEntitySearch";
import { searchDeals } from "@/features/deals/api/dealEntitySearch";
import { searchLeads } from "@/features/leads/api/leadEntitySearch";
import { searchStaff } from "@/features/staff/api/staffEntitySearch";

import type { Activity } from "../types";

import {
  activityFormSchema,
  activityPriorityOptions,
  activityStatusOptions,
  activityTypeOptions,
  type ActivityFormInput,
  type ActivityFormValues,
} from "./activityFormSchema";

interface ActivityFormProps {
  activity?: Activity;
  readOnly?: boolean;
  onSubmit(values: ActivityFormValues): Promise<void>;
}

const emptyValues: ActivityFormValues = {
  title: "",
  description: "",
  activity_type: "task",
  status: "planned",
  priority: "medium",
  due_date: "",
  owner_id: null,
  content_type: "",
  object_id: "",
};

export function ActivityForm({
  activity,
  onSubmit,
  readOnly = false,
}: ActivityFormProps) {
  const {
    register,
    handleSubmit,
    reset,
    resetField,
    control,
    formState: { errors, isSubmitting },
  } = useForm<ActivityFormInput, unknown, ActivityFormValues>({
    resolver: zodResolver(activityFormSchema),
    defaultValues: emptyValues,
  });

  // ---------------------------------------------------------------------------
  // Watch content type
  // ---------------------------------------------------------------------------

  const contentType = useWatch({
    control,
    name: "content_type",
  });

  // ---------------------------------------------------------------------------
  // Load activity into form
  // ---------------------------------------------------------------------------

  useEffect(() => {
    if (!activity) {
      reset(emptyValues);
      return;
    }

    reset({
      title: activity.title ?? "",
      description: activity.description ?? "",

      activity_type: activity.activity_type,
      status: activity.status,
      priority: activity.priority,

      due_date: activity.due_date ? activity.due_date.slice(0, 16) : "",

      owner_id: activity.owner ? String(activity.owner.id) : null,

      content_type: activity.content_type_name ?? "",
      object_id: activity.object_id ?? "",
    });
  }, [activity, reset]);

  // ---------------------------------------------------------------------------
  // Owner name
  // ---------------------------------------------------------------------------

  const ownerName = activity?.owner
    ? `${activity.owner.first_name ?? ""} ${
        activity.owner.last_name ?? ""
      }`.trim()
    : "";

  // ---------------------------------------------------------------------------
  // Submit
  // ---------------------------------------------------------------------------

  const handleFormSubmit = async (values: ActivityFormValues) => {
    await onSubmit(values);
  };

  return (
    <form onSubmit={handleSubmit(handleFormSubmit)} className="space-y-6">
      {/* ------------------------------------------------------------------ */}
      {/* Basic information */}
      {/* ------------------------------------------------------------------ */}

      <section className="space-y-4">
        <div>
          <h3 className="text-sm font-semibold">Basic information</h3>

          <p className="text-sm text-muted-foreground">
            Activity details and scheduling information.
          </p>
        </div>

        <div className="grid grid-cols-2 gap-4">
          {/* Title */}
          <div className="col-span-2 space-y-1.5">
            <label htmlFor="title" className="text-sm font-medium">
              Title
            </label>

            <input
              id="title"
              {...register("title")}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
              placeholder="Activity title"
              readOnly={readOnly}
            />

            {errors.title && (
              <p className="text-sm text-destructive">{errors.title.message}</p>
            )}
          </div>

          {/* Activity type */}
          <div className="space-y-1.5">
            <label htmlFor="activity_type" className="text-sm font-medium">
              Activity type
            </label>

            <select
              id="activity_type"
              {...register("activity_type")}
              disabled={readOnly}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
            >
              {activityTypeOptions.map((option) => (
                <option key={option.value} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>

            {errors.activity_type && (
              <p className="text-sm text-destructive">
                {errors.activity_type.message}
              </p>
            )}
          </div>

          {/* Status */}
          <div className="space-y-1.5">
            <label htmlFor="status" className="text-sm font-medium">
              Status
            </label>

            <select
              id="status"
              {...register("status")}
              disabled={readOnly}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
            >
              {activityStatusOptions.map((option) => (
                <option key={option.value} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>

            {errors.status && (
              <p className="text-sm text-destructive">
                {errors.status.message}
              </p>
            )}
          </div>

          {/* Priority */}
          <div className="space-y-1.5">
            <label htmlFor="priority" className="text-sm font-medium">
              Priority
            </label>

            <select
              id="priority"
              {...register("priority")}
              disabled={readOnly}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
            >
              {activityPriorityOptions.map((option) => (
                <option key={option.value} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>

            {errors.priority && (
              <p className="text-sm text-destructive">
                {errors.priority.message}
              </p>
            )}
          </div>

          {/* Due date */}
          <div className="space-y-1.5">
            <label htmlFor="due_date" className="text-sm font-medium">
              Due date
            </label>

            <input
              id="due_date"
              type="datetime-local"
              {...register("due_date")}
              disabled={readOnly}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
            />

            {errors.due_date && (
              <p className="text-sm text-destructive">
                {errors.due_date.message}
              </p>
            )}
          </div>
        </div>
      </section>

      {/* ------------------------------------------------------------------ */}
      {/* Assignment */}
      {/* ------------------------------------------------------------------ */}

      <section className="space-y-4">
        <div>
          <h3 className="text-sm font-semibold">Assignment</h3>

          <p className="text-sm text-muted-foreground">
            Assign this activity to a staff member.
          </p>
        </div>

        <Controller
          name="owner_id"
          control={control}
          render={({ field, fieldState }) => (
            <EntityCombobox
              label="Owner"
              value={field.value}
              selectedOption={entityOption(activity?.owner?.id, ownerName)}
              onChange={field.onChange}
              searchFn={searchStaff}
              placeholder="Select owner..."
              searchPlaceholder="Search staff..."
              disabled={readOnly}
              error={fieldState.error?.message}
            />
          )}
        />
      </section>

      {/* ------------------------------------------------------------------ */}
      {/* Related record */}
      {/* ------------------------------------------------------------------ */}

      <section className="space-y-4">
        <div>
          <h3 className="text-sm font-semibold">Related record</h3>

          <p className="text-sm text-muted-foreground">
            Connect this activity to a CRM record.
          </p>
        </div>

        <div className="grid grid-cols-2 gap-4">
          {/* Content type */}
          <div className="space-y-1.5">
            <Controller
              name="content_type"
              control={control}
              render={({ field, fieldState }) => (
                <>
                  <label htmlFor="content_type" className="text-sm font-medium">
                    Related to
                  </label>

                  <select
                    id="content_type"
                    value={field.value}
                    onChange={(event) => {
                      field.onChange(event.target.value);

                      resetField("object_id");
                    }}
                    disabled={readOnly}
                    className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
                  >
                    <option value="">Select record type</option>

                    <option value="contact">Contact</option>

                    <option value="company">Company</option>

                    <option value="lead">Lead</option>

                    <option value="deal">Deal</option>
                  </select>

                  {fieldState.error && (
                    <p className="text-sm text-destructive">
                      {fieldState.error.message}
                    </p>
                  )}
                </>
              )}
            />
          </div>

          {/* Related object */}
          <Controller
            name="object_id"
            control={control}
            render={({ field, fieldState }) => {
              if (!contentType) {
                return (
                  <div className="space-y-1.5">
                    <label className="text-sm font-medium">Record</label>

                    <div className="flex h-10 items-center rounded-lg border bg-muted px-3 text-sm text-muted-foreground">
                      Select a record type first
                    </div>
                  </div>
                );
              }

              if (contentType === "contact") {
                return (
                  <EntityCombobox
                    label="Contact"
                    value={field.value}
                    selectedOption={entityOption(
                      activity?.object_id,
                      activity?.content_object_name ?? "",
                    )}
                    onChange={field.onChange}
                    searchFn={searchContacts}
                    placeholder="Select contact..."
                    searchPlaceholder="Search contacts..."
                    disabled={readOnly}
                    error={fieldState.error?.message}
                  />
                );
              }

              if (contentType === "company") {
                return (
                  <EntityCombobox
                    label="Company"
                    value={field.value}
                    selectedOption={entityOption(
                      activity?.object_id,
                      activity?.content_object_name ?? "",
                    )}
                    onChange={field.onChange}
                    searchFn={searchCompanies}
                    placeholder="Select company..."
                    searchPlaceholder="Search companies..."
                    disabled={readOnly}
                    error={fieldState.error?.message}
                  />
                );
              }

              if (contentType === "lead") {
                return (
                  <EntityCombobox
                    label="Lead"
                    value={field.value}
                    selectedOption={entityOption(
                      activity?.object_id,
                      activity?.content_object_name ?? "",
                    )}
                    onChange={field.onChange}
                    searchFn={searchLeads}
                    placeholder="Select lead..."
                    searchPlaceholder="Search leads..."
                    disabled={readOnly}
                    error={fieldState.error?.message}
                  />
                );
              }

              if (contentType === "deal") {
                return (
                  <EntityCombobox
                    label="Deal"
                    value={field.value}
                    selectedOption={entityOption(
                      activity?.object_id,
                      activity?.content_object_name ?? "",
                    )}
                    onChange={field.onChange}
                    searchFn={searchDeals}
                    placeholder="Select deal..."
                    searchPlaceholder="Search deals..."
                    disabled={readOnly}
                    error={fieldState.error?.message}
                  />
                );
              }

              return (
                <div className="space-y-1.5">
                  <label className="text-sm font-medium">Record</label>
                  <div className="flex h-10 items-center rounded-lg border border-yellow-500 bg-yellow-50 px-3 text-sm text-yellow-700">
                    Unsupported record type: {contentType}
                  </div>
                </div>
              );
            }}
          />
        </div>
      </section>

      {/* ------------------------------------------------------------------ */}
      {/* Description */}
      {/* ------------------------------------------------------------------ */}

      <section className="space-y-2">
        <label htmlFor="description" className="text-sm font-medium">
          Description
        </label>

        <textarea
          id="description"
          {...register("description")}
          rows={5}
          className="w-full resize-none rounded-lg border bg-background p-3 text-sm outline-none focus:ring-2 focus:ring-ring"
          placeholder="Describe the activity..."
          readOnly={readOnly}
        />

        {errors.description && (
          <p className="text-sm text-destructive">
            {errors.description.message}
          </p>
        )}
      </section>

      {/* ------------------------------------------------------------------ */}
      {/* Actions */}
      {/* ------------------------------------------------------------------ */}

      {!readOnly && (
        <div className="sticky bottom-0 -mx-6 flex justify-end border-t bg-background px-6 py-4">
          <button
            type="submit"
            disabled={isSubmitting}
            className="inline-flex h-10 items-center justify-center rounded-lg bg-primary px-5 text-sm font-medium text-primary-foreground hover:bg-primary/90 disabled:pointer-events-none disabled:opacity-50"
          >
            {isSubmitting
              ? "Saving..."
              : activity
                ? "Save changes"
                : "Create activity"}
          </button>
        </div>
      )}
    </form>
  );
}
