import {
  Activity,
  Building2,
  Handshake,
  LayoutDashboard,
  StickyNote,
  Target,
  Users,
} from "lucide-react";

export interface SidebarItem {
  label: string;
  href: string;
  icon: React.ElementType;
}

export const sidebarItems: SidebarItem[] = [
  {
    label: "Dashboard",
    href: "/dashboard",
    icon: LayoutDashboard,
  },
  {
    label: "Companies",
    href: "/companies",
    icon: Building2,
  },
  {
    label: "Contacts",
    href: "/contacts",
    icon: Users,
  },
  {
    label: "Leads",
    href: "/leads",
    icon: Target,
  },
  {
    label: "Deals",
    href: "/deals",
    icon: Handshake,
  },
  {
    label: "Activities",
    href: "/activities",
    icon: Activity,
  },
  {
    label: "Notes",
    href: "/notes",
    icon: StickyNote,
  },
];
