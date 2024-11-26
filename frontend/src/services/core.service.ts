import { getCookie } from '../utils/cookies.utils';

const SERVER_URL = "http://localhost:8000/api"

const createHeaders = () => {
  const headers = new Headers()

  headers.append("Content-Type", "application/json")

  const token = getCookie("token")

  if (token) {
    headers.append("Authorization", `Bearer ${token}`)
  }

  return headers
}

export const keep_alive= async (token: string) => {
  const url = new URL(SERVER_URL + "/users/user/info");

  const headers = createHeaders();

  if (headers.has("Authorization")) {
    headers.delete("Authorization");
  }

  headers.append("Authorization", `Bearer ${token}`)

  return await fetch(url, {
    method: "GET",
    headers
  });
}

export const get = async (uri: string, params: URLSearchParams | null = null) => {
  const url = new URL(SERVER_URL + uri);
  let query = "";

  if (params) {
    query = "?" + params
  }

  return await fetch(url + query, {
    method: "GET",
    headers: createHeaders()
  });
}

export const post = async (uri: string, body: any) => {
  const url = new URL(SERVER_URL + uri);

  return await fetch(url, {
    method: 'POST',
    headers: createHeaders(),
    body: JSON.stringify(body)
  });
}

export const put = async (uri: string, body: any) => {
  const url = new URL(SERVER_URL + uri);

  return await fetch(url, {
    method: 'PUT',
    headers: createHeaders(),
    body: JSON.stringify(body)
  });
}

export const patch = async (uri: string, body: any) => {
  const url = new URL(SERVER_URL + uri);

  return await fetch(url, {
    method: 'PATCH',
    headers: createHeaders(),
    body: JSON.stringify(body)
  });
}

export const remove = async (uri: string) => {
  const url = new URL(SERVER_URL + uri);

  return await fetch(url, {
    method: 'DELETE',
    headers: createHeaders()
  });
}