const SERVER_URL = "http://localhost:8000/api"

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

  return await fetch(url + query); 
}

export const post = async (uri: string, body: any) => {
  const url = new URL(SERVER_URL + uri);

  return await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(convertNumbers(body))
  });
}