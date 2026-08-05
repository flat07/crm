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
    permission: "dashboard.view",
    icon: LayoutDashboard,
  },
  {
    title: "Companies",
    href: "/staff/companies",
    permission: "company.view",
    icon: Building2,
  },
  {
    title: "Contacts",
    href: "/staff/contacts",
    permission: "contact.view",
    icon: Users,
  },
  {
    title: "Leads",
    href: "/staff/leads",
    permission: "lead.view",
    icon: UserPlus,
  },
  {
    title: "Deals",
    href: "/staff/deals",
    permission: "deal.view",
    icon: Handshake,
  },
  {
    title: "Activities",
    href: "/staff/activities",
    permission: "activity.view",
    icon: CalendarDays,
  },
  {
    title: "Profile",
    href: "/staff/profile",
    permission: "user.view",
    icon: User,
  },
];
