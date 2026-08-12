// frontend/src/features/companies/pages/CompaniesPage.tsx
import { DataGrid } from "@/components/shared/DataGrid";
import { getCompanies } from "../api/companyApi";
import {
  createCompany,
  deleteCompany,
  updateCompany,
} from "../api/companyMutations";
import { CompanyForm } from "../components/CompanyForm";
import { companyColumns } from "../components/companyColumns";
import type { Company } from "../types";

export default function CompaniesPage() {
  return (
    <DataGrid<Company>
      queryKey={["companies"]}
      queryFn={getCompanies}
      columns={companyColumns}
      title="Companies"
      searchPlaceholder="Search companies..."
      actions={{
        view: true,
        edit: true,
        delete: true,
        onDelete: async (company) => {
          // console.log("🔍 [CompaniesPage] Deleting company:", company);
          await deleteCompany(company.id);
          // console.log("🔍 [CompaniesPage] Company deleted successfully");
        },
      }}
      onCreate={(onSuccess) => {
        // console.log("🔍 [CompaniesPage] Render create form");
        return (
          <CompanyForm
            onSubmit={async (values) => {
              // console.log(
              //   "🔍 [CompaniesPage] Create form submitted with values:",
              //   values,
              // );
              try {
                await createCompany(values);
                // console.log("🔍 [CompaniesPage] Company created successfully");
                await onSuccess();
                // console.log(
                //   "🔍 [CompaniesPage] onSuccess called, drawer should close",
                // );
              } catch (error) {
                // console.error("🔍 [CompaniesPage] Create failed:", error);
              }
            }}
          />
        );
      }}
      renderForm={(company, mode, onSuccess) => {
        // console.log("🔍 [CompaniesPage] renderForm called:", {
        //   company,
        //   mode,
        //   hasCompany: !!company,
        // });

        if (!company) {
          // console.log("🔍 [CompaniesPage] No company, returning null");
          return null;
        }

        if (mode === "view") {
          // console.log("🔍 [CompaniesPage] Rendering view mode");
          return (
            <CompanyForm company={company} readOnly onSubmit={async () => {}} />
          );
        }

        // console.log("🔍 [CompaniesPage] Rendering edit mode");
        return (
          <CompanyForm
            company={company}
            onSubmit={async (values) => {
              console.log(
                "🔍 [CompaniesPage] Edit form submitted with values:",
                values,
              );
              console.log("🔍 [CompaniesPage] Company ID:", company.id);
              try {
                await updateCompany(company.id, values);
                console.log("🔍 [CompaniesPage] Company updated successfully");
                await onSuccess();
                console.log(
                  "🔍 [CompaniesPage] onSuccess called, drawer should close",
                );
              } catch (error) {
                console.error("🔍 [CompaniesPage] Update failed:", error);
              }
            }}
          />
        );
      }}
      drawerTitle={(_row, mode) => {
        if (mode === "create") {
          return "Create Company";
        }
        if (mode === "view") {
          return "Company Details";
        }
        return "Edit Company";
      }}
    />
  );
}
