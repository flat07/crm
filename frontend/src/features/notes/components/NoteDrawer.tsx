// frontend/src/features/notes/components/NoteDrawer.tsx

import { zodResolver } from "@hookform/resolvers/zod";
import { X } from "lucide-react";
import { useEffect } from "react";
import { Controller, useForm, useWatch } from "react-hook-form";

import { EntityCombobox } from "@/components/shared/DataGrid/form";

import { entityOption } from "@/components/shared/DataGrid/form/entityOption";

import { searchCompanies } from "@/features/companies/api/companyEntitySearch";
import { searchContacts } from "@/features/contacts/api/contactEntitySearch";
import { searchDeals } from "@/features/deals/api/dealEntitySearch";
import { searchLeads } from "@/features/leads/api/leadEntitySearch";

import type { Note } from "../types";

import {
  noteContentTypeOptions,
  noteFormSchema,
  type NoteFormInput,
  type NoteFormValues,
} from "../components/noteFormSchema";

interface NoteDrawerProps {
  open: boolean;
  note?: Note | null;
  onClose: () => void;
  onSubmit: (values: NoteFormValues) => Promise<void>;
}

const emptyValues: NoteFormValues = {
  title: "",
  content: "",
  content_type: "company",
  object_id: "",
  is_pinned: false,
  is_private: false,
};

export function NoteDrawer({ open, note, onClose, onSubmit }: NoteDrawerProps) {
  const {
    register,
    handleSubmit,
    reset,
    resetField,
    control,
    formState: { errors, isSubmitting },
  } = useForm<NoteFormInput, unknown, NoteFormValues>({
    resolver: zodResolver(noteFormSchema),
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
  // Load note
  // ---------------------------------------------------------------------------

  useEffect(() => {
    if (!open) {
      return;
    }

    if (!note) {
      reset(emptyValues);
      return;
    }

    reset({
      title: note.title ?? "",
      content: note.content ?? "",
      content_type: note.content_type,
      object_id: note.object_id ? String(note.object_id) : "",
      is_pinned: note.is_pinned,
      is_private: note.is_private,
    });
  }, [open, note, reset]);

  // ---------------------------------------------------------------------------
  // Submit
  // ---------------------------------------------------------------------------

  const submit = async (values: NoteFormValues) => {
    await onSubmit(values);
  };

  // ---------------------------------------------------------------------------
  // Selected entity
  // ---------------------------------------------------------------------------

  const selectedEntity = note?.object_display
    ? entityOption(note.object_id, note.object_display)
    : undefined;

  if (!open) {
    return null;
  }

  return (
    <div className="fixed inset-0 z-50">
      {/* Overlay */}
      <button
        type="button"
        aria-label="Close"
        onClick={onClose}
        className="absolute inset-0 bg-black/30"
      />

      {/* Drawer */}
      <aside className="absolute right-0 top-0 flex h-full w-full max-w-xl flex-col border-l bg-background shadow-xl">
        {/* Header */}
        <div className="flex h-16 items-center justify-between border-b px-6">
          <div>
            <h2 className="font-semibold">{note ? "Edit Note" : "Add Note"}</h2>

            <p className="text-sm text-muted-foreground">
              {note ? "Update this note." : "Create a new note."}
            </p>
          </div>

          <button
            type="button"
            onClick={onClose}
            className="rounded-md p-2 hover:bg-muted"
          >
            <X className="h-5 w-5" />
          </button>
        </div>

        {/* Form */}
        <form
          onSubmit={handleSubmit(submit)}
          className="flex flex-1 flex-col overflow-hidden"
        >
          <div className="flex-1 space-y-5 overflow-y-auto p-6">
            {/* ---------------------------------------------------------------- */}
            {/* Title */}
            {/* ---------------------------------------------------------------- */}

            <div className="space-y-1.5">
              <label htmlFor="note-title" className="text-sm font-medium">
                Title
              </label>

              <input
                id="note-title"
                {...register("title")}
                placeholder="Note title"
                className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
              />

              {errors.title && (
                <p className="text-sm text-destructive">
                  {errors.title.message}
                </p>
              )}
            </div>

            {/* ---------------------------------------------------------------- */}
            {/* Content */}
            {/* ---------------------------------------------------------------- */}

            <div className="space-y-1.5">
              <label htmlFor="note-content" className="text-sm font-medium">
                Content
              </label>

              <textarea
                id="note-content"
                {...register("content")}
                rows={8}
                placeholder="Write your note..."
                className="w-full resize-none rounded-lg border bg-background p-3 text-sm outline-none focus:ring-2 focus:ring-ring"
              />

              {errors.content && (
                <p className="text-sm text-destructive">
                  {errors.content.message}
                </p>
              )}
            </div>

            {/* ---------------------------------------------------------------- */}
            {/* Related record */}
            {/* ---------------------------------------------------------------- */}

            <section className="space-y-4">
              <div>
                <h3 className="text-sm font-semibold">Related record</h3>

                <p className="text-sm text-muted-foreground">
                  Connect this note to a CRM record.
                </p>
              </div>

              {/* Record type */}
              <div className="space-y-1.5">
                <label
                  htmlFor="note-content-type"
                  className="text-sm font-medium"
                >
                  Related to
                </label>

                <Controller
                  name="content_type"
                  control={control}
                  render={({ field, fieldState }) => (
                    <>
                      <select
                        id="note-content-type"
                        value={field.value}
                        onChange={(event) => {
                          field.onChange(event.target.value);

                          // Clear selected UUID when changing
                          // Company -> Contact, etc.
                          resetField("object_id");
                        }}
                        className="h-10 w-full rounded-lg border bg-background px-3 text-sm outline-none focus:ring-2 focus:ring-ring"
                      >
                        {noteContentTypeOptions.map((option) => (
                          <option key={option.value} value={option.value}>
                            {option.label}
                          </option>
                        ))}
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

              {/* Record */}
              <Controller
                name="object_id"
                control={control}
                render={({ field, fieldState }) => {
                  if (contentType === "company") {
                    return (
                      <EntityCombobox
                        label="Company"
                        value={field.value}
                        selectedOption={selectedEntity}
                        onChange={field.onChange}
                        searchFn={searchCompanies}
                        placeholder="Select company..."
                        searchPlaceholder="Search companies..."
                        error={fieldState.error?.message}
                      />
                    );
                  }

                  if (contentType === "contact") {
                    return (
                      <EntityCombobox
                        label="Contact"
                        value={field.value}
                        selectedOption={selectedEntity}
                        onChange={field.onChange}
                        searchFn={searchContacts}
                        placeholder="Select contact..."
                        searchPlaceholder="Search contacts..."
                        error={fieldState.error?.message}
                      />
                    );
                  }

                  if (contentType === "lead") {
                    return (
                      <EntityCombobox
                        label="Lead"
                        value={field.value}
                        selectedOption={selectedEntity}
                        onChange={field.onChange}
                        searchFn={searchLeads}
                        placeholder="Select lead..."
                        searchPlaceholder="Search leads..."
                        error={fieldState.error?.message}
                      />
                    );
                  }

                  if (contentType === "deal") {
                    return (
                      <EntityCombobox
                        label="Deal"
                        value={field.value}
                        selectedOption={selectedEntity}
                        onChange={field.onChange}
                        searchFn={searchDeals}
                        placeholder="Select deal..."
                        searchPlaceholder="Search deals..."
                        error={fieldState.error?.message}
                      />
                    );
                  }

                  return (
                    <div className="space-y-1.5">
                      <label className="text-sm font-medium">Record</label>

                      <div className="flex h-10 items-center rounded-lg border bg-muted px-3 text-sm text-muted-foreground">
                        Select a record type first
                      </div>
                    </div>
                  );
                }}
              />
            </section>

            {/* ---------------------------------------------------------------- */}
            {/* Options */}
            {/* ---------------------------------------------------------------- */}

            <section className="space-y-3">
              <h3 className="text-sm font-semibold">Options</h3>

              <label className="flex items-center gap-3">
                <input
                  type="checkbox"
                  {...register("is_pinned")}
                  className="h-4 w-4 rounded border"
                />

                <span className="text-sm">Pin this note</span>
              </label>

              <label className="flex items-center gap-3">
                <input
                  type="checkbox"
                  {...register("is_private")}
                  className="h-4 w-4 rounded border"
                />

                <span className="text-sm">Private note</span>
              </label>
            </section>
          </div>

          {/* Footer */}
          <div className="flex justify-end gap-3 border-t bg-background px-6 py-4">
            <button
              type="button"
              onClick={onClose}
              className="h-10 rounded-lg border px-4 text-sm font-medium hover:bg-muted"
            >
              Cancel
            </button>

            <button
              type="submit"
              disabled={isSubmitting}
              className="h-10 rounded-lg bg-primary px-4 text-sm font-medium text-primary-foreground hover:bg-primary/90 disabled:opacity-50"
            >
              {isSubmitting
                ? "Saving..."
                : note
                  ? "Save changes"
                  : "Create note"}
            </button>
          </div>
        </form>
      </aside>
    </div>
  );
}
