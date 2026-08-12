// frontend/src/features/contacts/pages/ContactsPage.tsx

import { DataGrid } from "@/components/shared/DataGrid";

import { getContacts } from "../api/contactApi";

import { ContactForm } from "../components/ContactForm";
import { contactColumns } from "../components/contactColumns";

import {
  useCreateContact,
  useDeleteContact,
  useUpdateContact,
} from "../hooks/useContactMutations";

import type { Contact } from "../types";

export default function ContactsPage() {
  const createContactMutation = useCreateContact();
  const deleteContactMutation = useDeleteContact();
  const updateContactMutation = useUpdateContact();

  return (
    <DataGrid<Contact>
      queryKey={["contacts"]}
      queryFn={getContacts}
      columns={contactColumns}
      title="Contacts"
      searchPlaceholder="Search contacts..."
      actions={{
        view: true,
        edit: true,
        delete: true,

        onDelete: async (contact) => {
          deleteContactMutation.mutate(contact.id);
        },
      }}

      // -----------------------------------------------------------------------
      // Create
      // -----------------------------------------------------------------------

      onCreate={(onSuccess) => {
        return (
          <ContactForm
            onSubmit={async (values) => {
              createContactMutation.mutate(values, {
                onSuccess: async () => {
                  await onSuccess();
                },
              });
            }}
          />
        );
      }}

      // -----------------------------------------------------------------------
      // View / Edit
      // -----------------------------------------------------------------------

      renderForm={(contact, mode, onSuccess) => {
        if (!contact) {
          return null;
        }

        // View
        if (mode === "view") {
          return (
            <ContactForm contact={contact} readOnly onSubmit={async () => {}} />
          );
        }

        // Edit
        return (
          <ContactForm
            contact={contact}
            onSubmit={async (values) => {
              updateContactMutation.mutate(
                {
                  id: contact.id,
                  contactData: values,
                },
                {
                  onSuccess: async () => {
                    await onSuccess();
                  },
                },
              );
            }}
          />
        );
      }}

      // -----------------------------------------------------------------------
      // Drawer title
      // -----------------------------------------------------------------------

      drawerTitle={(_row, mode) => {
        if (mode === "create") {
          return "Create Contact";
        }

        if (mode === "view") {
          return "Contact Details";
        }

        return "Edit Contact";
      }}
    />
  );
}
