// frontend/src/features/companies/components/CompanyActivities.tsx

import { Plus } from "lucide-react";
import { useState } from "react";

import { Button } from "@/components/ui/button";
import { RelatedActivityForm } from "@/features/activities/components/RelatedActivityForm";
import { useActivities } from "@/features/activities/hooks/useActivities";

interface CompanyActivitiesProps {
  companyId: string;
}

export function CompanyActivities({ companyId }: CompanyActivitiesProps) {
  const [showForm, setShowForm] = useState(false);

  const { data, isLoading, isError } = useActivities({
    content_type: "company",
    object_id: companyId,
  });

  if (isLoading) {
    return (
      <section className="space-y-4">
        <h3 className="text-sm font-semibold">Activities</h3>

        <p className="text-sm text-muted-foreground">Loading activities...</p>
      </section>
    );
  }

  if (isError) {
    return (
      <section className="space-y-4">
        <h3 className="text-sm font-semibold">Activities</h3>

        <p className="text-sm text-destructive">Failed to load activities.</p>
      </section>
    );
  }

  const activities = data?.results ?? [];

  return (
    <section className="space-y-4">
      <div className="flex items-start justify-between gap-4">
        <div>
          <h3 className="text-sm font-semibold">Activities</h3>

          <p className="text-sm text-muted-foreground">
            Calls, emails, meetings, tasks, and other activities.
          </p>
        </div>

        <Button type="button" size="sm" onClick={() => setShowForm(true)}>
          <Plus className="mr-2 h-4 w-4" />
          Add activity
        </Button>
      </div>

      {showForm && (
        <div className="rounded-lg border p-4">
          <RelatedActivityForm
            contentType="company"
            objectId={companyId}
            onSuccess={() => setShowForm(false)}
            onCancel={() => setShowForm(false)}
          />
        </div>
      )}

      {activities.length === 0 ? (
        <div className="rounded-lg border p-6 text-center">
          <p className="text-sm text-muted-foreground">No activities yet.</p>
        </div>
      ) : (
        <div className="space-y-3">
          {activities.map((activity) => (
            <div key={activity.id} className="rounded-lg border p-4">
              <div className="flex items-start justify-between gap-4">
                <div>
                  <h4 className="text-sm font-medium">{activity.title}</h4>

                  <p className="text-sm text-muted-foreground">
                    {activity.activity_type}
                  </p>
                </div>

                <span className="text-xs text-muted-foreground">
                  {activity.status}
                </span>
              </div>

              {activity.description && (
                <p className="mt-2 text-sm">{activity.description}</p>
              )}
            </div>
          ))}
        </div>
      )}
    </section>
  );
}
