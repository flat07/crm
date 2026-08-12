// frontend/src/lib/axios.ts

import { API_BASE_URL } from "@/config/api";
import axios from "axios";

import { refreshToken } from "@/features/auth/api/refresh";
import {
  clearTokens,
  getAccessToken,
  getRefreshToken,
  setAccessToken,
} from "@/features/auth/utils/token";

export const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    "Content-Type": "application/json",
  },
});

api.interceptors.request.use((config) => {
  // console.log("🚀 AXIOS REQUEST");
  // console.log("URL:", config.url);
  // console.log("METHOD:", config.method);
  // console.log("DATA:", config.data);

  const token = getAccessToken();

  const isPublic = config.url?.startsWith("/public/");

  if (token && !isPublic) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});
let isRefreshing = false;

let queue: {
  resolve: (token: string) => void;
  reject: (error: unknown) => void;
}[] = [];

function processQueue(error: unknown, token?: string) {
  queue.forEach((promise) => {
    if (error) {
      promise.reject(error);
    } else {
      promise.resolve(token!);
    }
  });

  queue = [];
}

api.interceptors.response.use(
  (response) => {
    // console.log("✅ AXIOS RESPONSE");
    // console.log("STATUS:", response.status);
    // console.log("URL:", response.config.url);
    // console.log("DATA:", response.data);

    return response;
  },

  async (error) => {
    // console.log("🔥🔥🔥 AXIOS RESPONSE ERROR 🔥🔥🔥");

    // console.log("ERROR:", error);
    // console.log("STATUS:", error.response?.status);
    // console.log("URL:", error.config?.url);
    // console.log("DATA:", error.response?.data);
    const original = error.config;

    if (error.response?.status !== 401 || original._retry) {
      // console.log("➡️ NOT A 401 — REJECTING ERROR BACK TO CALLER");
      return Promise.reject(error);
    }
    // console.log("🔐 401 — starting token refresh");

    original._retry = true;

    if (isRefreshing) {
      // console.log("⏳ Token refresh already running");
      return new Promise((resolve, reject) => {
        queue.push({
          resolve: (token) => {
            original.headers.Authorization = `Bearer ${token}`;

            resolve(api(original));
          },
          reject,
        });
      });
    }

    isRefreshing = true;

    try {
      // console.log("🔄 Refreshing access token...");
      const refresh = getRefreshToken();

      if (!refresh) {
        // console.log("❌ No refresh token");
        throw error;
      }

      const data = await refreshToken(refresh);
      // console.log("✅ Token refreshed");

      setAccessToken(data.access);

      processQueue(null, data.access);

      original.headers.Authorization = `Bearer ${data.access}`;

      return api(original);
    } catch (err) {
      // console.log("❌ Token refresh failed:", err);
      processQueue(err);

      clearTokens();

      window.location.href = "/login";

      return Promise.reject(err);
    } finally {
      isRefreshing = false;
    }
  },
);
