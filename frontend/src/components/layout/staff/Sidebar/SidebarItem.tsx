import { NavLink } from "react-router-dom";
import type { SidebarItem as SidebarItemType } from "./sidebarConfig";

interface SidebarItemProps {
  item: SidebarItemType;
}

export function SidebarItem({ item }: SidebarItemProps) {
  const Icon = item.icon;

  return (
    <NavLink
      to={item.href}
      className={({ isActive }) =>
        [
          "flex items-center gap-3 rounded-lg px-3 py-2.5",
          "text-sm font-medium transition-colors",
          isActive
            ? "bg-primary text-primary-foreground"
            : "text-muted-foreground hover:bg-muted hover:text-foreground",
        ].join(" ")
      }
    >
      <Icon className="h-4 w-4 shrink-0" />

      <span>{item.label}</span>
    </NavLink>
  );
}
