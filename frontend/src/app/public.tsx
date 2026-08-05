// src/routes/public.tsx

import PublicLayout from "@/components/layout/PublicLayout";

function Home() {
  return <h1>Home</h1>;
}

export const publicRoutes = [
  {
    element: <PublicLayout />,
    children: [
      {
        path: "/",
        element: <Home />,
      },
    ],
  },
];
