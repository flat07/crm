// frontend/src/features/contacts/components/ContactForm.tsx
import { zodResolver } from "@hookform/resolvers/zod";
import { useEffect } from "react";
import { Controller, useForm } from "react-hook-form";

import { EntityCombobox } from "@/components/shared/DataGrid/form";

import { searchCompanies } from "@/features/companies/api/companyEntitySearch";
import { searchStaff } from "@/features/staff/api/staffEntitySearch";

import type { Contact } from "../types";

import {
  contactFormSchema,
  contactSourceOptions,
  contactTypeOptions,
  type ContactFormInput,
  type ContactFormValues,
} from "./contactFormSchema";

interface ContactFormProps {
  contact?: Contact;
  readOnly?: boolean;
  onSubmit(values: ContactFormValues): Promise<void>;
}

const emptyValues: ContactFormValues = {
  first_name: "",
  last_name: "",
  job_title: "",
  email: "",
  phone: "",
  mobile: "",
  contact_type: "",
  source: "",
  company: null,
  owner: null,
  notes: "",
  birthday: "",
  linkedin_url: "",
  address: "",
  city: "",
  country: "",
};

export function ContactForm({
  contact,
  onSubmit,
  readOnly = false,
}: ContactFormProps) {
  const {
    register,
    handleSubmit,
    reset,
    control,
    formState: { errors, isSubmitting },
  } = useForm<ContactFormInput, unknown, ContactFormValues>({
    resolver: zodResolver(contactFormSchema),

    defaultValues: emptyValues,
  });

  useEffect(() => {
    if (!contact) {
      reset(emptyValues);
      return;
    }

    reset({
      first_name: contact.first_name ?? "",
      last_name: contact.last_name ?? "",
      job_title: contact.job_title ?? "",
      email: contact.email ?? "",
      phone: contact.phone ?? "",
      mobile: contact.mobile ?? "",

      contact_type: (contact.contact_type ??
        "") as ContactFormValues["contact_type"],

      source: (contact.source ?? "") as ContactFormValues["source"],

      company: contact.company ?? null,
      owner: contact.owner ?? null,

      notes: contact.notes ?? "",
      birthday: contact.birthday ?? "",
      linkedin_url: contact.linkedin_url ?? "",
      address: contact.address ?? "",
      city: contact.city ?? "",
      country: contact.country ?? "",
    });
  }, [contact, reset]);

  return (
    <form
      onSubmit={onSubmit ? handleSubmit(onSubmit) : undefined}
      className="space-y-6"
    >
      {/* ------------------------------------------------------------------ */}
      {/* Basic information */}
      {/* ------------------------------------------------------------------ */}

      <section className="space-y-4">
        <div>
          <h3 className="text-sm font-semibold">Basic information</h3>

          <p className="text-sm text-muted-foreground">
            Contact identity and contact information.
          </p>
        </div>

        <div className="grid grid-cols-2 gap-4">
          {/* First name */}
          <div className="space-y-1.5">
            <label htmlFor="first_name" className="text-sm font-medium">
              First name
            </label>

            <input
              id="first_name"
              {...register("first_name")}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
              placeholder="First name"
              readOnly={readOnly}
            />

            {errors.first_name && (
              <p className="text-sm text-destructive">
                {errors.first_name.message}
              </p>
            )}
          </div>

          {/* Last name */}
          <div className="space-y-1.5">
            <label htmlFor="last_name" className="text-sm font-medium">
              Last name
            </label>

            <input
              id="last_name"
              {...register("last_name")}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
              placeholder="Last name"
              readOnly={readOnly}
            />

            {errors.last_name && (
              <p className="text-sm text-destructive">
                {errors.last_name.message}
              </p>
            )}
          </div>

          {/* Job title */}
          <div className="space-y-1.5">
            <label htmlFor="job_title" className="text-sm font-medium">
              Job title
            </label>

            <input
              id="job_title"
              {...register("job_title")}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
              placeholder="Job title"
              readOnly={readOnly}
            />

            {errors.job_title && (
              <p className="text-sm text-destructive">
                {errors.job_title.message}
              </p>
            )}
          </div>

          {/* Email */}
          <div className="space-y-1.5">
            <label htmlFor="email" className="text-sm font-medium">
              Email
            </label>

            <input
              id="email"
              type="email"
              {...register("email")}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
              placeholder="contact@example.com"
              readOnly={readOnly}
            />

            {errors.email && (
              <p className="text-sm text-destructive">{errors.email.message}</p>
            )}
          </div>

          {/* Phone */}
          <div className="space-y-1.5">
            <label htmlFor="phone" className="text-sm font-medium">
              Phone
            </label>

            <input
              id="phone"
              {...register("phone")}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
              placeholder="+998..."
              readOnly={readOnly}
            />

            {errors.phone && (
              <p className="text-sm text-destructive">{errors.phone.message}</p>
            )}
          </div>

          {/* Mobile */}
          <div className="space-y-1.5">
            <label htmlFor="mobile" className="text-sm font-medium">
              Mobile
            </label>

            <input
              id="mobile"
              {...register("mobile")}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
              placeholder="+998..."
              readOnly={readOnly}
            />

            {errors.mobile && (
              <p className="text-sm text-destructive">
                {errors.mobile.message}
              </p>
            )}
          </div>
        </div>
      </section>

      {/* ------------------------------------------------------------------ */}
      {/* Contact details */}
      {/* ------------------------------------------------------------------ */}

      <section className="space-y-4">
        <div>
          <h3 className="text-sm font-semibold">Contact details</h3>
        </div>

        <div className="grid grid-cols-2 gap-4">
          {/* Contact type */}
          <div className="space-y-1.5">
            <label htmlFor="contact_type" className="text-sm font-medium">
              Contact type
            </label>

            <select
              id="contact_type"
              {...register("contact_type")}
              disabled={readOnly}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
            >
              <option value="">Select contact type</option>

              {contactTypeOptions.map((option) => (
                <option key={option.value} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>

            {errors.contact_type && (
              <p className="text-sm text-destructive">
                {errors.contact_type.message}
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
              <option value="">Select source</option>

              {contactSourceOptions.map((option) => (
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

          {/* Company */}
          <div className="space-y-1.5">
            <Controller
              name="company"
              control={control}
              render={({ field, fieldState }) => (
                <EntityCombobox
                  label="Company"
                  value={field.value}
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

          {/* Owner */}
          <div className="space-y-1.5">
            <Controller
              name="owner"
              control={control}
              render={({ field, fieldState }) => (
                <EntityCombobox
                  label="Owner"
                  value={field.value}
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

          {/* Birthday */}
          <div className="space-y-1.5">
            <label htmlFor="birthday" className="text-sm font-medium">
              Birthday
            </label>

            <input
              id="birthday"
              type="date"
              {...register("birthday")}
              disabled={readOnly}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
            />

            {errors.birthday && (
              <p className="text-sm text-destructive">
                {errors.birthday.message}
              </p>
            )}
          </div>

          {/* LinkedIn */}
          <div className="space-y-1.5">
            <label htmlFor="linkedin_url" className="text-sm font-medium">
              LinkedIn
            </label>

            <input
              id="linkedin_url"
              {...register("linkedin_url")}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
              placeholder="https://linkedin.com/in/..."
              readOnly={readOnly}
            />

            {errors.linkedin_url && (
              <p className="text-sm text-destructive">
                {errors.linkedin_url.message}
              </p>
            )}
          </div>
        </div>
      </section>

      {/* ------------------------------------------------------------------ */}
      {/* Address */}
      {/* ------------------------------------------------------------------ */}

      <section className="space-y-4">
        <div>
          <h3 className="text-sm font-semibold">Address</h3>
        </div>

        <div className="space-y-4">
          <input
            {...register("address")}
            placeholder="Address"
            readOnly={readOnly}
            className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
          />

          <div className="grid grid-cols-2 gap-4">
            <input
              {...register("city")}
              placeholder="City"
              readOnly={readOnly}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
            />

            <input
              {...register("country")}
              placeholder="Country"
              readOnly={readOnly}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
            />
          </div>
        </div>
      </section>

      {/* ------------------------------------------------------------------ */}
      {/* Notes */}
      {/* ------------------------------------------------------------------ */}

      <section className="space-y-2">
        <label htmlFor="notes" className="text-sm font-medium">
          Notes
        </label>

        <textarea
          id="notes"
          {...register("notes")}
          rows={4}
          className="w-full resize-none rounded-lg border bg-background p-3 text-sm outline-none focus:ring-2 focus:ring-ring"
          placeholder="Notes about the contact..."
          readOnly={readOnly}
        />

        {errors.notes && (
          <p className="text-sm text-destructive">{errors.notes.message}</p>
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
              : contact
                ? "Save changes"
                : "Create contact"}
          </button>
        </div>
      )}
    </form>
  );
}
