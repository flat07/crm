// frontend/src/lib/queryKeys.ts
export const queryKeys = {
  auth: {
    me: ["auth", "me"] as const,
  },

  companies: {
    all: ["companies"] as const,

    list: (page: number, search: string, ordering: string) =>
      ["companies", page, search, ordering] as const,

    detail: (id: number) => ["companies", id] as const,
  },

  contacts: {
    all: ["contacts"] as const,
    list: (page: number, search: string, ordering: string) =>
      ["contacts", page, search, ordering] as const,

    detail: (id: number) => ["contacts", id] as const,
  },
  deals: {
    all: ["deals"] as const,

    list: (page: number, search: string, ordering: string) =>
      ["deals", "list", page, search, ordering] as const,

    detail: (id: number) => ["deals", "detail", id] as const,
  },
};
