// frontend/src/features/auth/pages/LoginPage.tsx

import { Card, CardContent } from "@/components/ui/card";
import { Navigate } from "react-router-dom";
import { toast } from "sonner";

import { useAuth } from "@/contexts/AuthContext";

import LoginForm from "../components/LoginForm";
import { useLogin } from "../hooks/useLogin";

export default function LoginPage() {
  const mutation = useLogin();

  const auth = useAuth();

  async function handleSubmit(values: { email: string; password: string }) {
    try {
      const tokens = await mutation.mutateAsync(values);

      await auth.login(tokens.access, tokens.refresh);
      // console.log("DEBUG: LoginPage ");
      // 2. Success toast notification
      toast.success("Welcome back!", {
        description: "You have logged in successfully.",
      });
    } catch (error: any) {
      // 3. Error toast notification
      toast.error("Login failed", {
        description:
          error?.response?.data?.message ||
          error?.message ||
          "Please check your credentials and try again.",
      });
    }
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
