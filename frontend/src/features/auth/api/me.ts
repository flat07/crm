// frontend/src/features/auth/api/me.ts

import { api } from "@/lib/axios";

import type { User } from "../types";

export async function me() {
  const { data } = await api.get<User>("/staff/auth/me/");

  return data;
}
