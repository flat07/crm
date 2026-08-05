// src/app/router.tsx

import { createBrowserRouter, RouterProvider } from "react-router-dom";

import NotFound from "@/components/shared/NotFound";

import { publicRoutes } from "./public";
import { staffRoutes } from "./staff";

const router = createBrowserRouter([
  ...publicRoutes,
  ...staffRoutes,
  {
    path: "*",
    element: <NotFound />,
  },
]);

export function AppRouter() {
  return <RouterProvider router={router} />;
}
