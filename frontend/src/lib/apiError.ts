// frontend/src/lib/apiError.ts

import axios from "axios";

type DjangoErrorResponse = {
  detail?: string;
  [field: string]: unknown;
};

function getValidationErrorMessage(data: DjangoErrorResponse): string | null {
  const messages: string[] = [];

  for (const [field, value] of Object.entries(data)) {
    if (field === "detail") {
      continue;
    }

    if (Array.isArray(value)) {
      for (const message of value) {
        if (typeof message === "string") {
          messages.push(`${field}: ${message}`);
        }
      }
    } else if (typeof value === "string") {
      messages.push(`${field}: ${value}`);
    }
  }

  if (messages.length === 0) {
    return null;
  }

  return messages.join("\n");
}

export function getApiErrorMessage(error: unknown): string {
  if (!axios.isAxiosError(error)) {
    return "Something went wrong. Please try again.";
  }

  const response = error.response;

  if (!response) {
    return "Unable to connect to the server.";
  }

  const data = response.data as DjangoErrorResponse;

  if (response.status === 400) {
    // Existing special case
    if (data.lead) {
      return "This lead already has a deal.";
    }

    // DRF detail error
    if (typeof data.detail === "string") {
      return data.detail;
    }

    // DRF field validation errors
    const validationMessage = getValidationErrorMessage(data);

    if (validationMessage) {
      return validationMessage;
    }

    return "Please check the information you entered.";
  }

  if (response.status === 401) {
    return "Your session has expired. Please log in again.";
  }

  if (response.status === 403) {
    return "You don't have permission to perform this action.";
  }

  if (response.status === 404) {
    return "The requested resource was not found.";
  }

  if (response.status >= 500) {
    return "Something went wrong on the server. Please try again later.";
  }

  return "Unable to complete the request.";
}
