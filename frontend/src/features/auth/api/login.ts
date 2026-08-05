// frontend/src/features/auth/api/login.ts

import { api } from "@/lib/axios";

import type { LoginRequest, LoginResponse } from "../types";

export async function login(payload: LoginRequest) {
  const { data } = await api.post<LoginResponse>("/staff/auth/login/", payload);

  return data;
}
