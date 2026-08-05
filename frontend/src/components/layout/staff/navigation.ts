import {
  Building2,
  CalendarDays,
  Handshake,
  LayoutDashboard,
  User,
  UserPlus,
  Users,
} from "lucide-react";

export const navigation = [
  {
    title: "Dashboard",
    href: "/staff/dashboard",
    icon: LayoutDashboard,
  },
  {
    title: "Companies",
    href: "/staff/companies",
    icon: Building2,
  },
  {
    title: "Contacts",
    href: "/staff/contacts",
    icon: Users,
  },
  {
    title: "Leads",
    href: "/staff/leads",
    icon: UserPlus,
  },
  {
    title: "Deals",
    href: "/staff/deals",
    icon: Handshake,
  },
  {
    title: "Activities",
    href: "/staff/activities",
    icon: CalendarDays,
  },
  {
    title: "Profile",
    href: "/staff/profile",
    icon: User,
  },
];
