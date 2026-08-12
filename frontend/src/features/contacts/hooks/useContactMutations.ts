//  frontend/src/features/contacts/hooks/useContactMutations.ts

import { getApiErrorMessage } from "@/lib/apiError";
import { queryKeys } from "@/lib/queryKeys";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { toast } from "sonner";
import {
  createContact,
  deleteContact,
  updateContact,
  type CreateContactData,
  type UpdateContactData,
} from "../api/contactApi";

// -----------------------------------------------------------------------------
// Create contact
// -----------------------------------------------------------------------------

export function useCreateContact() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (contactData: CreateContactData) => createContact(contactData),

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["contacts"],
      });
      toast.success("Contact created successfully.");
    },
    onError: (error) => {
      // console.log("🔥 MUTATION ERROR:", error);

      toast.error("Unable to create contact ", {
        description: getApiErrorMessage(error),
      });
    },
  });
}

// -----------------------------------------------------------------------------
// Update contact
// -----------------------------------------------------------------------------

export function useUpdateContact() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({
      id,
      contactData,
    }: {
      id: number;
      contactData: UpdateContactData;
    }) => updateContact(id, contactData),

    onSuccess: (updatedContact) => {
      queryClient.invalidateQueries({
        queryKey: queryKeys.contacts.all,
      });
      toast.success("Contact updated successfully.");

      queryClient.setQueryData(["contacts", updatedContact.id], updatedContact);
    },
    onError: (error) => {
      // console.error("🔥 UPDATE CONTACT ERROR:", error);

      toast.error("Unable to update contact", {
        description: getApiErrorMessage(error),
      });
    },
  });
}

// -----------------------------------------------------------------------------
// Delete / archive contact
// -----------------------------------------------------------------------------

export function useDeleteContact() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (id: number) => deleteContact(id),

    onSuccess: (_, id) => {
      queryClient.invalidateQueries({
        queryKey: queryKeys.contacts.all,
      });

      queryClient.removeQueries({
        queryKey: queryKeys.contacts.detail(id),
      });
      toast.success("Contact deleted successfully.");
    },
  });
}
