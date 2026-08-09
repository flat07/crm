export const queryKeys = {
  auth: {
    me: ["auth", "me"] as const,
  },

  companies: {
    all: ["companies"] as const,

    list: (page: number, search: string) =>
      ["companies", page, search] as const,

    detail: (id: number) => ["companies", id] as const,
  },

  contacts: {
    all: ["contacts"] as const,
  },
};
