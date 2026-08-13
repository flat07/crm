import { SidebarItem } from "./SidebarItem";
import { sidebarItems } from "./sidebarConfig";

export function Sidebar() {
  return (
    <aside className="hidden w-64 shrink-0 border-r bg-background lg:block">
      <div className="flex h-full flex-col">
        {/* Sidebar Header */}
        <div className="flex h-16 items-center border-b px-6">
          <span className="text-lg font-semibold">CRM</span>
        </div>

        {/* Navigation */}
        <nav className="flex-1 space-y-1 p-4">
          {sidebarItems.map((item) => (
            <SidebarItem key={item.href} item={item} />
          ))}
        </nav>
      </div>
    </aside>
  );
}
