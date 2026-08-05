// frontend/src/features/auth/pages/LoginPage.test.tsx
import { screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import { renderWithProviders } from "@/test/render";

import LoginPage from "./LoginPage";

describe("LoginPage", () => {
  it("renders login form", () => {
    renderWithProviders(<LoginPage />);

    expect(screen.getByText("HotelBoard")).toBeInTheDocument();

    expect(screen.getByPlaceholderText(/username/i)).toBeInTheDocument();

    expect(screen.getByPlaceholderText(/password/i)).toBeInTheDocument();

    expect(
      screen.getByRole("button", {
        name: /login/i,
      }),
    ).toBeInTheDocument();
  });
});
