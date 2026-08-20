// frontend/src/features/leads/components/LeadPipelineColumn.tsx

import { useDroppable } from "@dnd-kit/core";

import type { Lead, LeadStatus } from "../types";
import { LeadPipelineCard } from "./LeadPipelineCard";

interface LeadPipelineColumnProps {
  status: LeadStatus;
  title: string;
  leads: Lead[];
}

export function LeadPipelineColumn({
  status,
  title,
  leads,
}: LeadPipelineColumnProps) {
  const { setNodeRef, isOver } = useDroppable({
    id: status,
    data: {
      status,
    },
  });

  const totalValue = leads.reduce((total, lead) => {
    return total + Number(lead.estimated_value ?? 0);
  }, 0);

  return (
    <div
      ref={setNodeRef}
      className={`flex min-w-[280px] flex-1 flex-col rounded-lg bg-muted/40 transition ${
        isOver ? "ring-2 ring-primary" : ""
      }`}
    >
      {/* Column header */}
      <div className="border-b p-4">
        <div className="flex items-center justify-between gap-3">
          <h3 className="text-sm font-semibold">{title}</h3>

          <span className="rounded-full bg-background px-2 py-1 text-xs text-muted-foreground">
            {leads.length}
          </span>
        </div>

        <p className="mt-1 text-xs text-muted-foreground">
          ${totalValue.toLocaleString()}
        </p>
      </div>

      {/* Cards */}
      <div className="flex min-h-[200px] flex-1 flex-col gap-3 p-3">
        {leads.length === 0 ? (
          <div className="rounded-lg border border-dashed p-6 text-center">
            <p className="text-xs text-muted-foreground">Drop leads here</p>
          </div>
        ) : (
          leads.map((lead) => <LeadPipelineCard key={lead.id} lead={lead} />)
        )}
      </div>
    </div>
  );
}
