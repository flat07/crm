// frontend/src/features/leads/components/LeadPipelineCard.tsx

import { useDraggable } from "@dnd-kit/core";
import { CSS } from "@dnd-kit/utilities";
import { ArrowUpRight } from "lucide-react";
import { useNavigate } from "react-router-dom";

import type { Lead } from "../types";

interface LeadPipelineCardProps {
  lead: Lead;
}

export function LeadPipelineCard({ lead }: LeadPipelineCardProps) {
  const navigate = useNavigate();

  const { attributes, listeners, setNodeRef, transform, isDragging } =
    useDraggable({
      id: lead.id,
      data: {
        lead,
      },
    });

  const style = {
    transform: CSS.Translate.toString(transform),
  };

  function handleClick() {
    if (isDragging) {
      return;
    }

    navigate(`/leads/${lead.id}`);
  }

  return (
    <div
      ref={setNodeRef}
      style={style}
      {...listeners}
      {...attributes}
      onClick={handleClick}
      className={`cursor-grab rounded-lg border bg-card p-4 shadow-sm transition hover:shadow-md ${
        isDragging ? "z-50 cursor-grabbing opacity-50 shadow-lg" : ""
      }`}
    >
      <div className="space-y-3">
        {/* Title */}
        <div>
          <h4 className="text-sm font-medium">{lead.title}</h4>

          {lead.company_name && (
            <p className="mt-1 text-xs text-muted-foreground">
              {lead.company_name}
            </p>
          )}
          <ArrowUpRight className="h-4 w-4 shrink-0 text-muted-foreground" />
        </div>

        {/* Contact */}
        {lead.contact_name && (
          <p className="text-xs text-muted-foreground">{lead.contact_name}</p>
        )}

        {/* Value / Probability */}
        <div className="flex items-center justify-between gap-4">
          <span className="text-sm font-medium">
            {lead.estimated_value
              ? `$${Number(lead.estimated_value).toLocaleString()}`
              : "—"}
          </span>

          <span className="text-xs text-muted-foreground">
            {lead.probability}%
          </span>
        </div>

        {/* Expected close */}
        {lead.expected_close_date && (
          <div className="text-xs text-muted-foreground">
            Close: {new Date(lead.expected_close_date).toLocaleDateString()}
          </div>
        )}

        {/* Owner */}
        {lead.owner_name && (
          <div className="border-t pt-3 text-xs text-muted-foreground">
            {lead.owner_name}
          </div>
        )}
      </div>
    </div>
  );
}
