import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";

import { AuthProvider, useAuth } from "./AuthContext";

import { me } from "@/features/auth/api/me";

import { getAccessToken } from "@/features/auth/utils/token";

vi.mock("@/features/auth/api/me", () => ({
  me: vi.fn(),
}));

vi.mock("@/features/auth/utils/token", () => ({
  getAccessToken: vi.fn(),
  setTokens: vi.fn(),
  clearTokens: vi.fn(),
}));

function TestComponent() {
  const auth = useAuth();

  return (
    <>
      <div>{auth.loading ? "Loading" : "Done"}</div>
      <div>{auth.isAuthenticated ? "User" : "Guest"}</div>
    </>
  );
}

describe("AuthProvider", () => {
  it("shows guest when there is no access token", async () => {
    vi.mocked(getAccessToken).mockReturnValue(null);

    render(
      <AuthProvider>
        <TestComponent />
      </AuthProvider>,
    );

    expect(await screen.findByText("Done")).toBeInTheDocument();
    expect(screen.getByText("Guest")).toBeInTheDocument();

    expect(me).not.toHaveBeenCalled();
  });
});
