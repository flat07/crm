// src/test/setup.ts

import "@testing-library/jest-dom/vitest";

import { vi } from "vitest";

// Polyfill ResizeObserver for Radix UI
class ResizeObserverMock {
  observe() {}
  unobserve() {}
  disconnect() {}
}

vi.stubGlobal("ResizeObserver", ResizeObserverMock);
