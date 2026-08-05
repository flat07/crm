// src/routes/ProtectedRoute.test.tsx

import { render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import { describe, expect, it, vi } from "vitest";

import ProtectedRoute from "./ProtectedRoute";

vi.mock("@/contexts/AuthContext", () => ({
  useAuth: vi.fn(),
}));

vi.mock("@/components/layout/staff/StaffMain", () => ({
  StaffMain: () => <div>Staff Dashboard</div>,
}));

vi.mock("@/components/shared/LoadingPage", () => ({
  default: () => <div>Loading...</div>,
}));

import { useAuth } from "@/contexts/AuthContext";

const mockedUseAuth = vi.mocked(useAuth);

describe("ProtectedRoute", () => {
  it("shows loading page while auth is loading", () => {
    mockedUseAuth.mockReturnValue({
      loading: true,
      isAuthenticated: false,
    } as never);

    render(
      <MemoryRouter>
        <ProtectedRoute />
      </MemoryRouter>,
    );

    expect(screen.getByText("Loading...")).toBeInTheDocument();
  });

  it("redirects unauthenticated users", () => {
    mockedUseAuth.mockReturnValue({
      loading: false,
      isAuthenticated: false,
    } as never);

    render(
      <MemoryRouter initialEntries={["/dashboard"]}>
        <ProtectedRoute />
      </MemoryRouter>,
    );

    expect(window.location.pathname).not.toBe("/dashboard");
  });

  it("renders protected layout for authenticated users", () => {
    mockedUseAuth.mockReturnValue({
      loading: false,
      isAuthenticated: true,
    } as never);

    render(
      <MemoryRouter>
        <ProtectedRoute />
      </MemoryRouter>,
    );

    expect(screen.getByText("Staff Dashboard")).toBeInTheDocument();
  });
});
