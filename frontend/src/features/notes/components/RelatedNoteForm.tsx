// frontend/src/features/companies/components/RelatedNoteForm.tsx

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";

import { useCreateNote } from "@/features/notes/hooks/useCreateNote";
import type { NoteContentType, NoteCreateInput } from "@/features/notes/types";

const relatedNoteSchema = z.object({
  title: z.string().optional(),
  content: z.string().min(1, "Content is required"),
  is_pinned: z.boolean(),
  is_private: z.boolean(),
});

type RelatedNoteFormValues = z.infer<typeof relatedNoteSchema>;

interface RelatedNoteFormProps {
  contentType: NoteContentType;
  objectId: string;
  onSuccess?: () => void;
  onCancel?: () => void;
}

export function RelatedNoteForm({
  contentType,
  objectId,
  onSuccess,
  onCancel,
}: RelatedNoteFormProps) {
  const createNote = useCreateNote();

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<RelatedNoteFormValues>({
    resolver: zodResolver(relatedNoteSchema),

    defaultValues: {
      title: "",
      content: "",
      is_pinned: false,
      is_private: false,
    },
  });

  async function handleFormSubmit(values: RelatedNoteFormValues) {
    const payload: NoteCreateInput = {
      title: values.title ?? "",
      content: values.content,

      content_type: contentType,
      object_id: objectId,

      is_pinned: values.is_pinned,
      is_private: values.is_private,
    };

    await createNote.mutateAsync(payload);

    reset();

    onSuccess?.();
  }

  const isSaving = isSubmitting || createNote.isPending;

  return (
    <div className="space-y-4">
      {/* Title */}
      <div className="space-y-2">
        <label htmlFor="note-title" className="text-sm font-medium">
          Title
        </label>

        <Input
          id="note-title"
          {...register("title")}
          placeholder="Note title"
        />

        {errors.title && (
          <p className="text-sm text-destructive">{errors.title.message}</p>
        )}
      </div>

      {/* Content */}
      <div className="space-y-2">
        <label htmlFor="note-content" className="text-sm font-medium">
          Note
        </label>

        <Textarea
          id="note-content"
          {...register("content")}
          placeholder="Write a note..."
          rows={5}
        />

        {errors.content && (
          <p className="text-sm text-destructive">{errors.content.message}</p>
        )}
      </div>

      {/* Options */}
      <div className="space-y-3">
        <label className="flex items-center gap-2 text-sm">
          <input
            type="checkbox"
            {...register("is_pinned")}
            className="h-4 w-4"
          />
          Pin this note
        </label>

        <label className="flex items-center gap-2 text-sm">
          <input
            type="checkbox"
            {...register("is_private")}
            className="h-4 w-4"
          />
          Private note
        </label>
      </div>

      {/* Actions */}
      <div className="flex justify-end gap-2">
        {onCancel && (
          <Button
            type="button"
            variant="outline"
            onClick={onCancel}
            disabled={isSaving}
          >
            Cancel
          </Button>
        )}

        <Button
          type="button"
          disabled={isSaving}
          onClick={handleSubmit(handleFormSubmit)}
        >
          {isSaving ? "Saving..." : "Add note"}
        </Button>
      </div>
    </div>
  );
}
