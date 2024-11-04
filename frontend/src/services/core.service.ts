const SERVER_URL = "http://localhost:8000/api"

export const get = async (uri: string, params: URLSearchParams | null = null) => {
  const url = new URL(SERVER_URL + uri);
  let query = "";

  if (params) {
    query = "?" + params
  }

  return await fetch(url + query); 
}