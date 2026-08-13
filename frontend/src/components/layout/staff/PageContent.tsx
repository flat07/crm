// frontend/src/components/layout/staff/PageContent.tsx
import type { ReactNode } from "react";

interface PageContentProps {
  children: ReactNode;
}

export function PageContent({ children }: PageContentProps) {
  return <div className="flex-1 overflow-auto p-6">{children}</div>;
}
