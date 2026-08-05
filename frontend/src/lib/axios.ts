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
  (response) => response,

  async (error) => {
    const original = error.config;

    if (error.response?.status !== 401 || original._retry) {
      return Promise.reject(error);
    }

    original._retry = true;

    if (isRefreshing) {
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
      const refresh = getRefreshToken();

      if (!refresh) {
        throw error;
      }

      const data = await refreshToken(refresh);

      setAccessToken(data.access);

      processQueue(null, data.access);

      original.headers.Authorization = `Bearer ${data.access}`;

      return api(original);
    } catch (err) {
      processQueue(err);

      clearTokens();

      window.location.href = "/login";

      return Promise.reject(err);
    } finally {
      isRefreshing = false;
    }
  },
);
