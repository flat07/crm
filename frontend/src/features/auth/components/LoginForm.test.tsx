// frontend/src/features/auth/components/LoginForm.test.tsx

import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";

import LoginForm from "./LoginForm";

describe("LoginForm", () => {
  it("renders username and password inputs", () => {
    render(<LoginForm isPending={false} onSubmit={vi.fn()} />);

    expect(screen.getByPlaceholderText(/username/i)).toBeInTheDocument();

    expect(screen.getByPlaceholderText(/password/i)).toBeInTheDocument();

    expect(screen.getByRole("button", { name: /login/i })).toBeInTheDocument();
  });

  it("allows typing into inputs", async () => {
    const user = userEvent.setup();

    render(<LoginForm isPending={false} onSubmit={vi.fn()} />);

    const username = screen.getByPlaceholderText(/username/i);
    const password = screen.getByPlaceholderText(/password/i);

    await user.type(username, "john");
    await user.type(password, "secret123");

    expect(username).toHaveValue("john");
    expect(password).toHaveValue("secret123");
  });

  it("calls onSubmit with valid form data", async () => {
    const user = userEvent.setup();

    const onSubmit = vi.fn();

    render(<LoginForm isPending={false} onSubmit={onSubmit} />);

    await user.type(screen.getByPlaceholderText(/username/i), "john");

    await user.type(screen.getByPlaceholderText(/password/i), "secret123");

    await user.click(screen.getByRole("button", { name: /login/i }));

    expect(onSubmit).toHaveBeenCalledTimes(1);
    // console.log(onSubmit.mock.calls);

    expect(onSubmit.mock.calls[0][0]).toMatchObject({
      username: "john",
      password: "secret123",
    });
    // expect(onSubmit).toHaveBeenCalledWith({
    //   username: "john",
    //   password: "secret123",
    // });
  });

  it("does not submit an invalid form", async () => {
    const user = userEvent.setup();

    const onSubmit = vi.fn();

    render(<LoginForm isPending={false} onSubmit={onSubmit} />);

    await user.click(screen.getByRole("button", { name: /login/i }));

    expect(onSubmit).not.toHaveBeenCalled();
  });

  it("disables submit button while pending", () => {
    render(<LoginForm isPending={true} onSubmit={vi.fn()} />);

    expect(screen.getByRole("button", { name: /login/i })).toBeDisabled();
  });
});
