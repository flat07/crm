// frontend/src/features/auth/schemas/loginSchema.ts

import { z } from "zod";

export const loginSchema = z.object({
  email: z.email({ message: "Invalid email address" }),
  password: z.string().min(1, { message: "Password is required" }),
});

export type LoginSchema = z.infer<typeof loginSchema>;
