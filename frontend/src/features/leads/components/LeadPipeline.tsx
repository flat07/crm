// frontend/src/features/leads/components/LeadPipeline.tsx

import {
  DndContext,
  DragEndEvent,
  DragOverlay,
  DragStartEvent,
  PointerSensor,
  useSensor,
  useSensors,
} from "@dnd-kit/core";
import { useEffect, useMemo, useState } from "react";
import { toast } from "sonner";

import { useLeads } from "@/features/leads/hooks/useLeads";
import { useUpdateLead } from "@/features/leads/hooks/useUpdateLead";

import type { Lead, LeadStatus } from "../types";
import { LeadPipelineCard } from "./LeadPipelineCard";
import { LeadPipelineColumn } from "./LeadPipelineColumn";

const PIPELINE_COLUMNS: {
  status: LeadStatus;
  title: string;
}[] = [
  {
    status: "new",
    title: "New",
  },
  {
    status: "contacted",
    title: "Contacted",
  },
  {
    status: "qualified",
    title: "Qualified",
  },
  {
    status: "won",
    title: "Won",
  },
];
const PIPELINE_STATUS_LABELS: Record<LeadStatus, string> = {
  new: "New",
  contacted: "Contacted",
  qualified: "Qualified",
  won: "Won",
};

export function LeadPipeline() {
  const [activeLead, setActiveLead] = useState<Lead | null>(null);
  const [pipelineLeads, setPipelineLeads] = useState<Lead[]>([]);

  const { data, isLoading, isError } = useLeads({
    page: 1,
    page_size: 100,
    is_active: true,
  });

  const updateLeadMutation = useUpdateLead();

  const sensors = useSensors(
    useSensor(PointerSensor, {
      activationConstraint: {
        distance: 8,
      },
    }),
  );

  /*
   * Keep local pipeline state synchronized with the server.
   */
  useEffect(() => {
    if (data?.results) {
      setPipelineLeads(data.results);
    }
  }, [data?.results]);

  const leadsByStatus = useMemo(() => {
    return PIPELINE_COLUMNS.reduce(
      (groups, column) => {
        groups[column.status] = pipelineLeads.filter(
          (lead) => lead.status === column.status,
        );

        return groups;
      },
      {} as Record<LeadStatus, Lead[]>,
    );
  }, [pipelineLeads]);

  function handleDragStart(event: DragStartEvent) {
    const lead = event.active.data.current?.lead as Lead | undefined;

    if (lead) {
      setActiveLead(lead);
    }
  }

  async function handleDragEnd(event: DragEndEvent) {
    setActiveLead(null);

    const { active, over } = event;

    if (!over) {
      return;
    }

    const lead = active.data.current?.lead as Lead | undefined;

    if (!lead) {
      return;
    }

    const newStatus = over.data.current?.status as LeadStatus | undefined;

    if (!newStatus || lead.status === newStatus) {
      return;
    }

    /*
     * Save the previous state so we can rollback
     * if the API request fails.
     */
    const previousLeads = pipelineLeads;

    /*
     * Optimistically move the card immediately.
     */
    setPipelineLeads((currentLeads) =>
      currentLeads.map((currentLead) =>
        currentLead.id === lead.id
          ? {
              ...currentLead,
              status: newStatus,
            }
          : currentLead,
      ),
    );

    try {
      await updateLeadMutation.mutateAsync({
        id: lead.id,
        data: {
          status: newStatus,
        },
      });

      toast.success(`Lead moved to ${PIPELINE_STATUS_LABELS[newStatus]}`);
    } catch {
      setPipelineLeads(previousLeads);

      toast.error("Failed to update lead status");
    }
  }

  function handleDragCancel() {
    setActiveLead(null);
  }

  if (isLoading) {
    return (
      <section className="space-y-4">
        <h2 className="text-lg font-semibold">Lead Pipeline</h2>

        <p className="text-sm text-muted-foreground">Loading pipeline...</p>
      </section>
    );
  }

  if (isError) {
    return (
      <section className="space-y-4">
        <h2 className="text-lg font-semibold">Lead Pipeline</h2>

        <p className="text-sm text-destructive">Failed to load leads.</p>
      </section>
    );
  }

  return (
    <section className="space-y-4">
      <div>
        <h2 className="text-lg font-semibold">Lead Pipeline</h2>

        <p className="text-sm text-muted-foreground">
          Drag leads between stages to update their status.
        </p>
      </div>

      <DndContext
        sensors={sensors}
        onDragStart={handleDragStart}
        onDragEnd={handleDragEnd}
        onDragCancel={handleDragCancel}
      >
        <div className="flex gap-4 overflow-x-auto pb-4">
          {PIPELINE_COLUMNS.map((column) => (
            <LeadPipelineColumn
              key={column.status}
              status={column.status}
              title={column.title}
              leads={leadsByStatus[column.status] ?? []}
            />
          ))}
        </div>

        <DragOverlay>
          {activeLead ? (
            <div className="rotate-2">
              <LeadPipelineCard lead={activeLead} />
            </div>
          ) : null}
        </DragOverlay>
      </DndContext>
    </section>
  );
}
