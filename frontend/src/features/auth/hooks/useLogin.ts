// frontend/src/features/auth/hooks/useLogin.ts

import { useMutation } from "@tanstack/react-query";

import { login as loginApi } from "../api/login";

export function useLogin() {
  return useMutation({
    mutationFn: loginApi,
  });
}
