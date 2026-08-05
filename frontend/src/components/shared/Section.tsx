// frontend/src/components/shared/Section.tsx

import type { PropsWithChildren } from "react";

interface Props extends PropsWithChildren {
  title?: string;
}

export default function Section({ title, children }: Props) {
  return (
    <section className="space-y-4">
      {title && <h3 className="text-lg font-semibold">{title}</h3>}

      {children}
    </section>
  );
}
