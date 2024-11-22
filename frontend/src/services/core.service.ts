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

const convertNumbers = (obj: any) : any => {
  if (Array.isArray(obj)) {
    return obj.map(convertNumbers);
  } else if (obj && typeof obj === 'object') {
    const newObj: any = {};
    for (const key in obj) {
      const value = obj[key];
      newObj[key] = typeof value === 'string' && !isNaN(Number(value)) ? Number(value) : value;
    }
    return newObj;
  }
  return obj;
};

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
    body: JSON.stringify(convertNumbers(body))
  });
}

export const post_literal = async (uri: string, body: any) => {
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
    body: JSON.stringify(convertNumbers(body))
  });
}

export const patch = async (uri: string, body: any) => {
  const url = new URL(SERVER_URL + uri);

  return await fetch(url, {
    method: 'PATCH',
    headers: createHeaders(),
    body: JSON.stringify(convertNumbers(body))
  });
}

export const remove = async (uri: string) => {
  const url = new URL(SERVER_URL + uri);

  return await fetch(url, {
    method: 'DELETE',
    headers: createHeaders()
  });
}