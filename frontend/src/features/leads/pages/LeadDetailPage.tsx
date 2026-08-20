// frontend/src/features/leads/pages/LeadDetailPage.tsx

import { useNavigate, useParams } from "react-router-dom";

import { ArrowLeft, Building2, Calendar, User, UserRound } from "lucide-react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";

import { useLead } from "../hooks/useLeads";

function formatDate(value: string | null) {
  if (!value) return "—";

  return new Date(value).toLocaleDateString();
}

function formatDateTime(value: string) {
  return new Date(value).toLocaleString();
}

function formatCurrency(value: string | null) {
  if (!value) return "—";

  const amount = Number(value);

  if (Number.isNaN(amount)) return value;

  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
  }).format(amount);
}

function getFullName(
  person: {
    first_name: string | null;
    last_name: string | null;
  } | null,
) {
  if (!person) return null;

  return [person.first_name, person.last_name].filter(Boolean).join(" ").trim();
}

function getStatusVariant(
  status: string,
): "default" | "secondary" | "outline" | "destructive" {
  switch (status) {
    case "won":
      return "default";

    case "qualified":
      return "secondary";

    case "contacted":
      return "outline";

    default:
      return "secondary";
  }
}

export function LeadDetailPage() {
  const navigate = useNavigate();
  const { id } = useParams<{ id: string }>();

  const { data: lead, isLoading, isError } = useLead(id ?? "");

  if (!id) {
    return (
      <div className="flex min-h-[400px] items-center justify-center">
        <div className="text-center">
          <h2 className="text-lg font-semibold">Lead not found</h2>

          <Button
            variant="outline"
            className="mt-4"
            onClick={() => navigate("/leads")}
          >
            Back to Leads
          </Button>
        </div>
      </div>
    );
  }

  if (isLoading) {
    return (
      <div className="space-y-6">
        <div className="h-8 w-48 animate-pulse rounded bg-muted" />

        <Card>
          <CardContent className="space-y-6 p-6">
            <div className="h-8 w-1/3 animate-pulse rounded bg-muted" />
            <div className="h-4 w-1/2 animate-pulse rounded bg-muted" />
            <div className="h-32 animate-pulse rounded bg-muted" />
          </CardContent>
        </Card>
      </div>
    );
  }

  if (isError || !lead) {
    return (
      <div className="flex min-h-[400px] items-center justify-center">
        <div className="text-center">
          <h2 className="text-lg font-semibold">Unable to load lead</h2>

          <p className="mt-1 text-sm text-muted-foreground">
            The lead may not exist or could not be loaded.
          </p>

          <Button
            variant="outline"
            className="mt-4"
            onClick={() => navigate("/leads")}
          >
            Back to Leads
          </Button>
        </div>
      </div>
    );
  }

  const contactName = getFullName(lead.contact) ?? lead.contact_name ?? "—";

  const ownerName = getFullName(lead.owner) ?? lead.owner_name ?? "—";

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between gap-4">
        <div className="flex items-center gap-3">
          <Button
            variant="ghost"
            size="icon"
            onClick={() => navigate("/leads")}
          >
            <ArrowLeft className="h-4 w-4" />
          </Button>

          <div>
            <div className="flex items-center gap-3">
              <h1 className="text-2xl font-semibold tracking-tight">
                {lead.title}
              </h1>

              <Badge variant={getStatusVariant(lead.status)}>
                {lead.status}
              </Badge>
            </div>

            <p className="mt-1 text-sm text-muted-foreground">
              Lead details and information
            </p>
          </div>
        </div>

        {/* <Button onClick={() => navigate(`/leads/${lead.id}/edit`)}>
          Edit Lead
        </Button> */}
      </div>

      {/* Main information */}
      <div className="grid gap-6 lg:grid-cols-3">
        {/* Overview */}
        <Card className="lg:col-span-2">
          <CardHeader>
            <CardTitle>Overview</CardTitle>
          </CardHeader>

          <CardContent className="space-y-6">
            <div className="grid gap-6 sm:grid-cols-2">
              <div>
                <p className="text-sm text-muted-foreground">Title</p>

                <p className="mt-1 font-medium">{lead.title}</p>
              </div>

              <div>
                <p className="text-sm text-muted-foreground">Status</p>

                <div className="mt-1">
                  <Badge variant={getStatusVariant(lead.status)}>
                    {lead.status}
                  </Badge>
                </div>
              </div>

              <div>
                <p className="text-sm text-muted-foreground">Source</p>

                <p className="mt-1 font-medium capitalize">
                  {lead.source?.replace("_", " ") ?? "—"}
                </p>
              </div>

              <div>
                <p className="text-sm text-muted-foreground">Estimated Value</p>

                <p className="mt-1 font-medium">
                  {formatCurrency(lead.estimated_value)}
                </p>
              </div>

              <div>
                <p className="text-sm text-muted-foreground">Probability</p>

                <p className="mt-1 font-medium">{lead.probability}%</p>
              </div>

              <div>
                <p className="text-sm text-muted-foreground">
                  Expected Close Date
                </p>

                <div className="mt-1 flex items-center gap-2">
                  <Calendar className="h-4 w-4 text-muted-foreground" />

                  <span className="font-medium">
                    {formatDate(lead.expected_close_date)}
                  </span>
                </div>
              </div>
            </div>

            <Separator />

            <div>
              <p className="text-sm text-muted-foreground">Description</p>

              <p className="mt-2 whitespace-pre-wrap text-sm leading-6">
                {lead.description || "No description provided."}
              </p>
            </div>
          </CardContent>
        </Card>

        {/* Lead summary */}
        <Card>
          <CardHeader>
            <CardTitle>Summary</CardTitle>
          </CardHeader>

          <CardContent className="space-y-5">
            <div>
              <p className="text-sm text-muted-foreground">Estimated Value</p>

              <p className="mt-1 text-xl font-semibold">
                {formatCurrency(lead.estimated_value)}
              </p>
            </div>

            <div>
              <p className="text-sm text-muted-foreground">Probability</p>

              <div className="mt-2">
                <div className="flex items-center justify-between text-sm">
                  <span>{lead.probability}%</span>
                </div>

                <div className="mt-2 h-2 overflow-hidden rounded-full bg-muted">
                  <div
                    className="h-full rounded-full bg-primary transition-all"
                    style={{
                      width: `${Math.min(Math.max(lead.probability, 0), 100)}%`,
                    }}
                  />
                </div>
              </div>
            </div>

            <div>
              <p className="text-sm text-muted-foreground">Status</p>

              <div className="mt-1">
                <Badge variant={getStatusVariant(lead.status)}>
                  {lead.status}
                </Badge>
              </div>
            </div>

            <div>
              <p className="text-sm text-muted-foreground">Active</p>

              <p className="mt-1 font-medium">
                {lead.is_active ? "Yes" : "No"}
              </p>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Related entities */}
      <div className="grid gap-6 md:grid-cols-3">
        {/* Company */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-base">
              <Building2 className="h-4 w-4" />
              Company
            </CardTitle>
          </CardHeader>

          <CardContent>
            {lead.company ? (
              <button
                type="button"
                className="text-left font-medium hover:underline"
                onClick={() =>
                  lead.company?.id && navigate(`/companies/${lead.company.id}`)
                }
              >
                {lead.company.name ?? lead.company_name ?? "—"}
              </button>
            ) : (
              <p className="text-sm text-muted-foreground">
                {lead.company_name ?? "No company"}
              </p>
            )}
          </CardContent>
        </Card>

        {/* Contact */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-base">
              <User className="h-4 w-4" />
              Contact
            </CardTitle>
          </CardHeader>

          <CardContent>
            {lead.contact ? (
              <button
                type="button"
                className="text-left font-medium hover:underline"
                onClick={() =>
                  lead.contact?.id && navigate(`/contacts/${lead.contact.id}`)
                }
              >
                {contactName}
              </button>
            ) : (
              <p className="text-sm text-muted-foreground">{contactName}</p>
            )}
          </CardContent>
        </Card>

        {/* Owner */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-base">
              <UserRound className="h-4 w-4" />
              Owner
            </CardTitle>
          </CardHeader>

          <CardContent>
            <p className="font-medium">{ownerName}</p>
          </CardContent>
        </Card>
      </div>

      {/* Metadata */}
      <Card>
        <CardHeader>
          <CardTitle>Metadata</CardTitle>
        </CardHeader>

        <CardContent>
          <div className="grid gap-6 sm:grid-cols-2">
            <div>
              <p className="text-sm text-muted-foreground">Created</p>

              <p className="mt-1 text-sm">{formatDateTime(lead.created_at)}</p>
            </div>

            <div>
              <p className="text-sm text-muted-foreground">Last Updated</p>

              <p className="mt-1 text-sm">{formatDateTime(lead.updated_at)}</p>
            </div>

            <div>
              <p className="text-sm text-muted-foreground">Lead ID</p>

              <p className="mt-1 break-all font-mono text-xs">{lead.id}</p>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
