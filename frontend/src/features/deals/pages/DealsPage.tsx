// frontend/src/features/deals/pages/DealsPage.tsx

import { DataGrid } from "@/components/shared/DataGrid";

import { getDeals } from "../api/dealsApi";
import { DealForm } from "../components/DealForm";
import { dealColumns } from "../components/dealColumns";
import { useCreateDeal } from "../hooks/useCreateDeal";
import { useDeleteDeal } from "../hooks/useDeleteDeal";
import { useUpdateDeal } from "../hooks/useUpdateDeal";

import type { Deal } from "../types";

export default function DealsPage() {
  const createDealMutation = useCreateDeal();
  const deleteDealMutation = useDeleteDeal();
  const updateDealMutation = useUpdateDeal();
  return (
    <DataGrid<Deal>
      queryKey={["deals"]}
      queryFn={getDeals}
      columns={dealColumns}
      title="Deals"
      searchPlaceholder="Search deals..."
      actions={{
        view: true,
        edit: true,
        delete: true,

        onDelete: async (deal) => {
          deleteDealMutation.mutate(deal.id);
        },
      }}
      onCreate={(onSuccess) => {
        return (
          <DealForm
            onSubmit={async (values) => {
              createDealMutation.mutate(values, {
                onSuccess: async () => {
                  await onSuccess();
                },
              });
            }}
          />
        );
      }}
      renderForm={(deal, mode, onSuccess) => {
        if (!deal) {
          return null;
        }

        if (mode === "view") {
          return <DealForm deal={deal} readOnly />;
        }

        return (
          <DealForm
            deal={deal}
            onSubmit={async (values) => {
              updateDealMutation.mutate(
                {
                  id: deal.id,
                  values,
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
          return "Create Deal";
        }

        if (mode === "view") {
          return "Deal Details";
        }

        return "Edit Deal";
      }}
    />
  );
}
