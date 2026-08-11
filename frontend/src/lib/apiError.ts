// frontend/src/lib/apiError.ts

import axios from "axios";

type DjangoErrorResponse = {
  detail?: string;
  [field: string]: unknown;
};

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
    if (data.lead) {
      return "This lead already has a deal.";
    }

    if (typeof data.detail === "string") {
      return data.detail;
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
