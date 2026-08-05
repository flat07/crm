// frontend/src/features/auth/pages/LoginPage.tsx

import { Navigate } from "react-router-dom";

import { Card, CardContent } from "@/components/ui/card";

import { useAuth } from "@/contexts/AuthContext";

import LoginForm from "../components/LoginForm";
import { useLogin } from "../hooks/useLogin";

export default function LoginPage() {
  const mutation = useLogin();

  const auth = useAuth();

  async function handleSubmit(values: { email: string; password: string }) {
    const tokens = await mutation.mutateAsync(values);

    await auth.login(tokens.access, tokens.refresh);
  }

  if (auth.isAuthenticated) {
    return <Navigate to="/dashboard" replace />;
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-muted">
      <Card className="w-full max-w-sm">
        <CardContent className="space-y-6 p-6">
          <div>
            <h1 className="text-2xl font-bold">HotelBoard</h1>

            <p className="text-muted-foreground">Staff Login</p>
          </div>

          <LoginForm isPending={mutation.isPending} onSubmit={handleSubmit} />
        </CardContent>
      </Card>
    </div>
  );
}
