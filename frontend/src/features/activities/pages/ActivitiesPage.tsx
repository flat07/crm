// frontend/src/features/activities/pages/ActivitiesPage.tsx

import { DataGrid } from "@/components/shared/DataGrid";

import { getActivities } from "../api/activitiesApi";

import { ActivityForm } from "../components/ActivityForm";
import { activityColumns } from "../components/activityColumns";

import { useCreateActivity } from "../hooks/useCreateActivity";
import { useDeleteActivity } from "../hooks/useDeleteActivity";
import { useUpdateActivity } from "../hooks/useUpdateActivity";
import { ActivityFormData } from "../types";

import type { Activity } from "../types";

export default function ActivitiesPage() {
  const createActivityMutation = useCreateActivity();
  const deleteActivityMutation = useDeleteActivity();
  const updateActivityMutation = useUpdateActivity();

  return (
    <DataGrid<Activity>
      queryKey={["activities"]}
      queryFn={getActivities}
      columns={activityColumns}
      title="Activities"
      searchPlaceholder="Search activities..."
      actions={{
        view: true,
        edit: true,
        delete: true,

        onDelete: async (activity) => {
          deleteActivityMutation.mutate(activity.id);
        },
      }}

      // -----------------------------------------------------------------------
      // Create
      // -----------------------------------------------------------------------

      onCreate={(onSuccess) => {
        return (
          <ActivityForm
            onSubmit={async (values) => {
              createActivityMutation.mutate(values as ActivityFormData, {
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

      renderForm={(activity, mode, onSuccess) => {
        if (!activity) {
          return null;
        }

        // View
        if (mode === "view") {
          return (
            <ActivityForm
              activity={activity}
              readOnly
              onSubmit={async () => {}}
            />
          );
        }

        // Edit
        return (
          <ActivityForm
            activity={activity}
            onSubmit={async (values) => {
              updateActivityMutation.mutate(
                {
                  id: activity.id,
                  values: values as any,
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
          return "Create Activity";
        }

        if (mode === "view") {
          return "Activity Details";
        }

        return "Edit Activity";
      }}
    />
  );
}
