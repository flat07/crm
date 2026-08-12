// frontend/src/features/leads/components/LeadForm.tsx

import { zodResolver } from "@hookform/resolvers/zod";
import { useEffect } from "react";
import { Controller, useForm } from "react-hook-form";

import { EntityCombobox } from "@/components/shared/DataGrid/form";
import { entityOption } from "@/components/shared/DataGrid/form/entityOption";

import { searchCompanies } from "@/features/companies/api/companyEntitySearch";
import { searchContacts } from "@/features/contacts/api/contactEntitySearch";
import { searchStaff } from "@/features/staff/api/staffEntitySearch";

import type { Lead } from "../types";

import {
  leadFormSchema,
  leadSourceOptions,
  leadStatusOptions,
  type LeadFormInput,
  type LeadFormValues,
} from "./leadFormSchema";

interface LeadFormProps {
  lead?: Lead;
  readOnly?: boolean;
  onSubmit(values: LeadFormValues): Promise<void>;
}

const emptyValues: LeadFormValues = {
  title: "",
  company: null,
  contact: null,
  owner: null,
  source: null,
  status: "new",
  estimated_value: null,
  probability: 0,
  expected_close_date: null,
  description: "",
  is_active: true,
};

export function LeadForm({ lead, onSubmit, readOnly = false }: LeadFormProps) {
  const {
    register,
    handleSubmit,
    reset,
    control,
    formState: { errors, isSubmitting },
  } = useForm<LeadFormInput, unknown, LeadFormValues>({
    resolver: zodResolver(leadFormSchema),
    defaultValues: emptyValues,
  });

  useEffect(() => {
    if (!lead) {
      reset(emptyValues);
      return;
    }

    reset({
      title: lead.title ?? "",
      company: lead.company?.id ? String(lead.company.id) : null,
      contact: lead.contact?.id ? String(lead.contact.id) : null,
      owner: lead.owner?.id ? String(lead.owner.id) : null,
      source: lead.source ?? null,
      status: lead.status,
      estimated_value: lead.estimated_value ?? null,
      probability: lead.probability ?? 0,
      expected_close_date: lead.expected_close_date ?? null,
      description: lead.description ?? "",
      is_active: lead.is_active ?? true,
    });
  }, [lead, reset]);

  return (
    <form
      onSubmit={onSubmit ? handleSubmit(onSubmit) : undefined}
      className="space-y-6"
    >
      {/* Lead information */}
      <section className="space-y-4">
        <div>
          <h3 className="text-sm font-semibold">Lead information</h3>

          <p className="text-sm text-muted-foreground">
            Basic information about the lead.
          </p>
        </div>

        <div className="grid grid-cols-2 gap-4">
          {/* Title */}
          <div className="space-y-1.5">
            <label htmlFor="title" className="text-sm font-medium">
              Title <span className="text-destructive">*</span>
            </label>

            <input
              id="title"
              type="text"
              {...register("title")}
              readOnly={readOnly}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
              placeholder="Enter lead title..."
            />

            {errors.title && (
              <p className="text-sm text-destructive">{errors.title.message}</p>
            )}
          </div>

          {/* Status */}
          <div className="space-y-1.5">
            <label htmlFor="status" className="text-sm font-medium">
              Status <span className="text-destructive">*</span>
            </label>

            <select
              id="status"
              {...register("status")}
              disabled={readOnly}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
            >
              {leadStatusOptions.map((option) => (
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

          {/* Source */}
          <div className="space-y-1.5">
            <label htmlFor="source" className="text-sm font-medium">
              Source
            </label>

            <select
              id="source"
              {...register("source")}
              disabled={readOnly}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
            >
              <option value="">Select source...</option>
              {leadSourceOptions.map((option) => (
                <option key={option.value} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>

            {errors.source && (
              <p className="text-sm text-destructive">
                {errors.source.message}
              </p>
            )}
          </div>

          {/* Estimated Value */}
          <div className="space-y-1.5">
            <label htmlFor="estimated_value" className="text-sm font-medium">
              Estimated Value
            </label>

            <input
              id="estimated_value"
              type="number"
              step="0.01"
              {...register("estimated_value")}
              readOnly={readOnly}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
              placeholder="0.00"
            />

            {errors.estimated_value && (
              <p className="text-sm text-destructive">
                {errors.estimated_value.message}
              </p>
            )}
          </div>

          {/* Probability */}
          <div className="space-y-1.5">
            <label htmlFor="probability" className="text-sm font-medium">
              Probability (%) <span className="text-destructive">*</span>
            </label>

            <input
              id="probability"
              type="number"
              min="0"
              max="100"
              {...register("probability", {
                valueAsNumber: true,
              })}
              readOnly={readOnly}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
              placeholder="0"
            />

            {errors.probability && (
              <p className="text-sm text-destructive">
                {errors.probability.message}
              </p>
            )}
          </div>

          {/* Expected Close Date */}
          <div className="space-y-1.5">
            <label
              htmlFor="expected_close_date"
              className="text-sm font-medium"
            >
              Expected Close Date
            </label>

            <input
              id="expected_close_date"
              type="date"
              {...register("expected_close_date")}
              disabled={readOnly}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
            />

            {errors.expected_close_date && (
              <p className="text-sm text-destructive">
                {errors.expected_close_date.message}
              </p>
            )}
          </div>
        </div>
      </section>

      {/* Relationships */}
      <section className="space-y-4">
        <div>
          <h3 className="text-sm font-semibold">Relationships</h3>

          <p className="text-sm text-muted-foreground">
            Connect this lead with a company, contact, and owner.
          </p>
        </div>

        <div className="grid grid-cols-2 gap-4">
          {/* Company */}
          <div className="space-y-1.5">
            <Controller
              name="company"
              control={control}
              render={({ field, fieldState }) => (
                <EntityCombobox
                  label="Company"
                  value={field.value ? String(field.value) : null}
                  selectedOption={entityOption(
                    lead?.company?.id ? String(lead.company.id) : null,
                    lead?.company?.name,
                  )}
                  onChange={(value) => {
                    field.onChange(value ? String(value) : null);
                  }}
                  searchFn={searchCompanies}
                  placeholder="Select company..."
                  searchPlaceholder="Search companies..."
                  disabled={readOnly}
                  error={fieldState.error?.message}
                />
              )}
            />

            {errors.company && (
              <p className="text-sm text-destructive">
                {errors.company.message}
              </p>
            )}
          </div>

          {/* Contact */}
          <div className="space-y-1.5">
            <Controller
              name="contact"
              control={control}
              render={({ field, fieldState }) => (
                <EntityCombobox
                  label="Contact"
                  value={field.value ? String(field.value) : null}
                  selectedOption={entityOption(
                    lead?.contact?.id ? String(lead.contact.id) : null,
                    `${lead?.contact?.first_name ?? ""} ${lead?.contact?.last_name ?? ""}`.trim(),
                  )}
                  onChange={(value) => {
                    field.onChange(value ? String(value) : null);
                  }}
                  searchFn={searchContacts}
                  placeholder="Select contact..."
                  searchPlaceholder="Search contacts..."
                  disabled={readOnly}
                  error={fieldState.error?.message}
                />
              )}
            />

            {errors.contact && (
              <p className="text-sm text-destructive">
                {errors.contact.message}
              </p>
            )}
          </div>

          {/* Owner */}
          <div className="space-y-1.5">
            <Controller
              name="owner"
              control={control}
              render={({ field, fieldState }) => (
                <EntityCombobox
                  label="Owner"
                  value={field.value ? String(field.value) : null}
                  selectedOption={entityOption(
                    lead?.owner?.id ? String(lead.owner.id) : null,
                    `${lead?.owner?.first_name ?? ""} ${lead?.owner?.last_name ?? ""}`.trim(),
                  )}
                  onChange={(value) => {
                    field.onChange(value ? String(value) : null);
                  }}
                  searchFn={searchStaff}
                  placeholder="Select owner..."
                  searchPlaceholder="Search staff..."
                  disabled={readOnly}
                  error={fieldState.error?.message}
                />
              )}
            />

            {errors.owner && (
              <p className="text-sm text-destructive">{errors.owner.message}</p>
            )}
          </div>
        </div>
      </section>

      {/* Description */}
      <section className="space-y-2">
        <label htmlFor="description" className="text-sm font-medium">
          Description
        </label>

        <textarea
          id="description"
          {...register("description")}
          rows={4}
          readOnly={readOnly}
          className="w-full resize-none rounded-lg border bg-background p-3 text-sm outline-none focus:ring-2 focus:ring-ring"
          placeholder="Notes about the lead..."
        />

        {errors.description && (
          <p className="text-sm text-destructive">
            {errors.description.message}
          </p>
        )}
      </section>

      {/* Status */}
      <label className="flex items-center gap-2">
        <input
          type="checkbox"
          {...register("is_active")}
          disabled={readOnly}
          className="h-4 w-4 rounded border"
        />

        <span className="text-sm font-medium">Active</span>
      </label>

      {/* Actions */}
      {!readOnly && (
        <div className="sticky bottom-0 -mx-6 flex justify-end border-t bg-background px-6 py-4">
          <button
            type="submit"
            disabled={isSubmitting}
            className="inline-flex h-10 items-center justify-center rounded-lg bg-primary px-5 text-sm font-medium text-primary-foreground hover:bg-primary/90 disabled:pointer-events-none disabled:opacity-50"
          >
            {isSubmitting ? "Saving..." : lead ? "Save changes" : "Create lead"}
          </button>
        </div>
      )}
    </form>
  );
}
