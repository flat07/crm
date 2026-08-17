// frontend/src/features/companies/components/CompanyForm.tsx
import { zodResolver } from "@hookform/resolvers/zod";
import { useEffect } from "react";
import { useForm } from "react-hook-form";
import type { Company } from "../types";
import { CompanyActivities } from "./CompanyActivities";
import { CompanyNotes } from "./CompanyNotes";
import {
  companyFormSchema,
  companySizeOptions,
  companyTypeOptions,
  industryOptions,
  type CompanyFormInput,
  type CompanyFormValues,
} from "./companyFormSchema";

interface CompanyFormProps {
  company?: Company;
  readOnly?: boolean;
  onSubmit(values: CompanyFormValues): Promise<void>;
}

const emptyValues: CompanyFormValues = {
  name: "",
  legal_name: "",
  website: "",
  email: "",
  phone: "",
  industry: "",
  company_type: "",
  size: "",
  tax_number: "",
  description: "",
  address: "",
  city: "",
  country: "",
  postal_code: "",
  owner: null,
  is_active: true,
};

export function CompanyForm({
  company,
  onSubmit,
  readOnly = false,
}: CompanyFormProps) {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<CompanyFormInput, unknown, CompanyFormValues>({
    resolver: zodResolver(companyFormSchema),

    defaultValues: emptyValues,
  });

  useEffect(() => {
    if (!company) {
      reset(emptyValues);
      return;
    }

    reset({
      name: company.name ?? "",
      legal_name: company.legal_name ?? "",
      website: company.website ?? "",
      email: company.email ?? "",
      phone: company.phone ?? "",
      industry: (company.industry ?? "") as CompanyFormValues["industry"],
      company_type: (company.company_type ??
        "") as CompanyFormValues["company_type"],
      size: (company.size ?? "") as CompanyFormValues["size"],
      tax_number: company.tax_number ?? "",
      description: company.description ?? "",
      address: company.address ?? "",
      city: company.city ?? "",
      country: company.country ?? "",
      postal_code: company.postal_code ?? "",
      owner: company.owner ?? null,
      is_active: company.is_active ?? true,
    });
  }, [company, reset]);

  return (
    <form
      onSubmit={onSubmit ? handleSubmit(onSubmit) : undefined}
      className="space-y-6"
    >
      {/* Basic information */}
      <section className="space-y-4">
        <div>
          <h3 className="text-sm font-semibold">Basic information</h3>

          <p className="text-sm text-muted-foreground">
            Company identity and contact information.
          </p>
        </div>

        <div className="space-y-4">
          {/* Name */}
          <div className="space-y-1.5">
            <label htmlFor="name" className="text-sm font-medium">
              Name
            </label>

            <input
              id="name"
              {...register("name")}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
              placeholder="Company name"
              readOnly={readOnly}
            />

            {errors.name && (
              <p className="text-sm text-destructive">{errors.name.message}</p>
            )}
          </div>

          {/* Website */}
          <div className="space-y-1.5">
            <label htmlFor="website" className="text-sm font-medium">
              Website
            </label>

            <input
              id="website"
              {...register("website")}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
              placeholder="https://example.com"
              readOnly={readOnly}
            />

            {errors.website && (
              <p className="text-sm text-destructive">
                {errors.website.message}
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
              placeholder="company@example.com"
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
        </div>
      </section>

      {/* Company details */}
      <section className="space-y-4">
        <div>
          <h3 className="text-sm font-semibold">Company details</h3>
        </div>

        <div className="grid grid-cols-2 gap-4">
          {/* Industry */}
          <div className="space-y-1.5">
            <label htmlFor="industry" className="text-sm font-medium">
              Industry
            </label>

            <select
              id="industry"
              {...register("industry")}
              disabled={readOnly}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
            >
              <option value="">Select industry</option>

              {industryOptions.map((option) => (
                <option key={option.value} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>
          </div>

          {/* Company type */}
          <div className="space-y-1.5">
            <label htmlFor="company_type" className="text-sm font-medium">
              Company type
            </label>

            <select
              id="company_type"
              {...register("company_type")}
              disabled={readOnly}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
            >
              <option value="">Select company type</option>

              {companyTypeOptions.map((option) => (
                <option key={option.value} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>
          </div>

          {/* Size */}
          <div className="space-y-1.5">
            <label htmlFor="size" className="text-sm font-medium">
              Size
            </label>

            <select
              id="size"
              {...register("size")}
              disabled={readOnly}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
            >
              <option value="">Select company size</option>

              {companySizeOptions.map((option) => (
                <option key={option.value} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>
          </div>

          {/* Tax number */}
          <div className="space-y-1.5">
            <label htmlFor="tax_number" className="text-sm font-medium">
              Tax number
            </label>

            <input
              id="tax_number"
              {...register("tax_number")}
              readOnly={readOnly}
              className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
            />
          </div>
        </div>
      </section>

      {/* Address */}
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

          <input
            {...register("postal_code")}
            placeholder="Postal code"
            readOnly={readOnly}
            className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
          />
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
          className="w-full resize-none rounded-lg border bg-background p-3 text-sm outline-none focus:ring-2 focus:ring-ring"
          placeholder="Notes about the company..."
        />
      </section>
      {/* Activities */}
      {company && <CompanyActivities companyId={String(company.id)} />}

      {/* Notes */}
      {company && <CompanyNotes companyId={String(company.id)} />}

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
            {isSubmitting
              ? "Saving..."
              : company
                ? "Save changes"
                : "Create company"}
          </button>
        </div>
      )}
    </form>
  );
}
