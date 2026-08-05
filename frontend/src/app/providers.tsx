// frontend/src/app/providers.tsx

import { Toaster } from "@/components/ui/sonner";
import { QueryClientProvider } from "@tanstack/react-query";
import { ThemeProvider } from "next-themes";

import { AuthProvider } from "@/contexts/AuthContext";
import { queryClient } from "@/lib/query-client";

type Props = {
  children: React.ReactNode;
};

export function AppProviders({ children }: Props) {
  return (
    <ThemeProvider
      attribute="class"
      defaultTheme="system"
      enableSystem
      disableTransitionOnChange
    >
      <QueryClientProvider client={queryClient}>
        <AuthProvider>
          {children}

          <Toaster richColors />
        </AuthProvider>
      </QueryClientProvider>
    </ThemeProvider>
  );
}
