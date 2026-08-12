// frontend/src/features/deals/components/DealForm.tsx

import { zodResolver } from "@hookform/resolvers/zod";
import { useEffect } from "react";
import { Controller, useForm } from "react-hook-form";

import { EntityCombobox } from "@/components/shared/DataGrid/form";
import { entityOption } from "@/components/shared/DataGrid/form/entityOption";

import { searchCompanies } from "@/features/companies/api/companyEntitySearch";
import { searchContacts } from "@/features/contacts/api/contactEntitySearch";
import { searchLeads } from "@/features/leads/api/leadEntitySearch";
import { searchStaff } from "@/features/staff/api/staffEntitySearch";

import type { Deal } from "../types";

import {
  dealFormSchema,
  dealStageOptions,
  type DealFormInput,
  type DealFormValues,
} from "./dealFormSchema";

interface DealFormProps {
  deal?: Deal;
  readOnly?: boolean;
  onSubmit(values: DealFormValues): Promise<void>;
}

const emptyValues: DealFormValues = {
  lead: null,
  company: null,
  contact: null,
  owner: null,

  stage: "prospecting",

  amount: "",
  probability: 0,

  expected_close_date: null,
  actual_close_date: null,

  description: "",

  is_active: true,
};

export function DealForm({ deal, onSubmit, readOnly = false }: DealFormProps) {
  const {
    register,
    handleSubmit,
    reset,
    control,
    formState: { errors, isSubmitting },
  } = useForm<DealFormInput, unknown, DealFormValues>({
    resolver: zodResolver(dealFormSchema),

    defaultValues: emptyValues,
  });

  useEffect(() => {
    if (!deal) {
      reset(emptyValues);
      return;
    }

    reset({
      lead: deal.lead ? String(deal.lead.id) : null,
      company: deal.company ? String(deal.company.id) : null,
      contact: deal.contact ? String(deal.contact.id) : null,
      owner: deal.owner ? String(deal.owner.id) : null,

      stage: deal.stage as DealFormValues["stage"],

      amount: deal.amount ?? "",
      probability: deal.probability ?? 0,

      expected_close_date: deal.expected_close_date ?? null,
      actual_close_date: deal.actual_close_date ?? null,

      description: deal.description ?? "",

      is_active: deal.is_active ?? true,
    });
  }, [deal, reset]);

  return (
    <form
      onSubmit={onSubmit ? handleSubmit(onSubmit) : undefined}
      className="space-y-6"
    >
      {/* Deal information */}
      <section className="space-y-4">
        <div>
          <h3 className="text-sm font-semibold">Deal information</h3>

          <p className="text-sm text-muted-foreground">
            Basic information about the sales opportunity.
          </p>
        </div>

        <div className="grid grid-cols-2 gap-4">
          {/* Stage */}
          <div className="space-y-1.5">
            <label htmlFor="stage" className="text-sm font-medium">
              Stage
            </label>

            <select
              id="stage"
              {...register("stage")}
              disabled={readOnly}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
            >
              {dealStageOptions.map((option) => (
                <option key={option.value} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>

            {errors.stage && (
              <p className="text-sm text-destructive">{errors.stage.message}</p>
            )}
          </div>

          {/* Amount */}
          <div className="space-y-1.5">
            <label htmlFor="amount" className="text-sm font-medium">
              Amount
            </label>

            <input
              id="amount"
              type="number"
              step="0.01"
              {...register("amount")}
              readOnly={readOnly}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
              placeholder="0.00"
            />

            {errors.amount && (
              <p className="text-sm text-destructive">
                {errors.amount.message}
              </p>
            )}
          </div>

          {/* Probability */}
          <div className="space-y-1.5">
            <label htmlFor="probability" className="text-sm font-medium">
              Probability (%)
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
        </div>
      </section>

      {/* Relationships */}
      <section className="space-y-4">
        <div>
          <h3 className="text-sm font-semibold">Relationships</h3>

          <p className="text-sm text-muted-foreground">
            Connect this deal with a lead, company, contact, and owner.
          </p>
        </div>

        <div className="grid grid-cols-2 gap-4">
          {/* Lead */}
          <div className="space-y-1.5">
            <Controller
              name="lead"
              control={control}
              render={({ field, fieldState }) => (
                <EntityCombobox
                  label="Lead"
                  value={field.value}
                  selectedOption={entityOption(
                    deal?.lead?.id,
                    `${deal?.lead?.title ?? ""}`.trim(),
                  )}
                  onChange={(value) => {
                    field.onChange(value);
                  }}
                  searchFn={searchLeads}
                  placeholder="Select lead..."
                  searchPlaceholder="Search leads..."
                  disabled={readOnly}
                  error={fieldState.error?.message}
                />
              )}
            />

            {errors.lead && (
              <p className="text-sm text-destructive">{errors.lead.message}</p>
            )}
          </div>

          {/* Company */}
          <div className="space-y-1.5">
            <Controller
              name="company"
              control={control}
              render={({ field, fieldState }) => (
                <EntityCombobox
                  label="Company"
                  value={field.value}
                  selectedOption={entityOption(
                    deal?.company?.id,
                    deal?.company?.name,
                  )}
                  onChange={(value) => {
                    field.onChange(value);
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
                  value={field.value}
                  selectedOption={entityOption(
                    deal?.contact?.id,
                    `${deal?.contact?.first_name ?? ""} ${deal?.contact?.last_name ?? ""}`.trim(),
                  )}
                  onChange={(value) => {
                    field.onChange(value);
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
                  value={field.value}
                  selectedOption={entityOption(
                    deal?.owner?.id,
                    `${deal?.owner?.first_name ?? ""} ${deal?.owner?.last_name ?? ""}`.trim(),
                  )}
                  onChange={(value) => {
                    field.onChange(value);
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

      {/* Closing dates */}
      <section className="space-y-4">
        <div>
          <h3 className="text-sm font-semibold">Closing dates</h3>
        </div>

        <div className="grid grid-cols-2 gap-4">
          {/* Expected close date */}
          <div className="space-y-1.5">
            <label
              htmlFor="expected_close_date"
              className="text-sm font-medium"
            >
              Expected close date
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

          {/* Actual close date */}
          <div className="space-y-1.5">
            <label htmlFor="actual_close_date" className="text-sm font-medium">
              Actual close date
            </label>

            <input
              id="actual_close_date"
              type="date"
              {...register("actual_close_date")}
              disabled={readOnly}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
            />

            {errors.actual_close_date && (
              <p className="text-sm text-destructive">
                {errors.actual_close_date.message}
              </p>
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
          placeholder="Notes about the deal..."
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
            {isSubmitting ? "Saving..." : deal ? "Save changes" : "Create deal"}
          </button>
        </div>
      )}
    </form>
  );
}
