import { DataGrid } from "@/components/shared/DataGrid";

import { getLeads } from "../api/leadsApi";
import { LeadForm } from "../components/LeadForm";
import { leadColumns } from "../components/leadColumns";
import { useCreateLead } from "../hooks/useCreateLead";
import { useDeleteLead } from "../hooks/useDeleteLead";
import { useUpdateLead } from "../hooks/useUpdateLead";

import type { Lead } from "../types";

export default function LeadsPage() {
  const createLeadMutation = useCreateLead();
  const deleteLeadMutation = useDeleteLead();
  const updateLeadMutation = useUpdateLead();

  return (
    <DataGrid<Lead>
      queryKey={["leads"]}
      queryFn={getLeads}
      columns={leadColumns}
      title="Leads"
      searchPlaceholder="Search leads..."
      actions={{
        view: true,
        edit: true,
        delete: true,

        onDelete: async (lead) => {
          deleteLeadMutation.mutate(String(lead.id));
        },
      }}
      onCreate={(onSuccess) => {
        return (
          <LeadForm
            onSubmit={async (values) => {
              createLeadMutation.mutate(values, {
                onSuccess: async () => {
                  await onSuccess();
                },
              });
            }}
          />
        );
      }}
      renderForm={(lead, mode, onSuccess) => {
        if (!lead) {
          return null;
        }

        if (mode === "view") {
          return <LeadForm lead={lead} readOnly onSubmit={async () => {}} />;
        }

        return (
          <LeadForm
            lead={lead}
            onSubmit={async (values) => {
              updateLeadMutation.mutate(
                {
                  id: String(lead.id),
                  data: values,
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
      drawerTitle={(_row, mode) => {
        if (mode === "create") {
          return "Create Lead";
        }

        if (mode === "view") {
          return "Lead Details";
        }

        return "Edit Lead";
      }}
    />
  );
}
