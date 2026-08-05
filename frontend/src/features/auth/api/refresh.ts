// frontend/src/features/auth/api/refresh.ts

import axios from "axios";

import { API_BASE_URL } from "@/config/api";

export interface RefreshResponse {
  access: string;
}

export async function refreshToken(refresh: string) {
  const { data } = await axios.post<RefreshResponse>(
    `${API_BASE_URL}/staff/auth/refresh/`,
    {
      refresh,
    },
  );

  return data;
}
