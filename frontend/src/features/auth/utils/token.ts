// frontend/src/features/auth/utils/token.ts

const ACCESS_TOKEN_KEY = "access_token";
const REFRESH_TOKEN_KEY = "refresh_token";

export function getAccessToken() {
  return localStorage.getItem(ACCESS_TOKEN_KEY);
}

export function getRefreshToken() {
  return localStorage.getItem(REFRESH_TOKEN_KEY);
}

export function setAccessToken(access: string) {
  localStorage.setItem(ACCESS_TOKEN_KEY, access);
}

export function setRefreshToken(refresh: string) {
  localStorage.setItem(REFRESH_TOKEN_KEY, refresh);
}

export function setTokens(access: string, refresh: string) {
  setAccessToken(access);
  setRefreshToken(refresh);
}

export function clearTokens() {
  localStorage.removeItem(ACCESS_TOKEN_KEY);

  localStorage.removeItem(REFRESH_TOKEN_KEY);
}
