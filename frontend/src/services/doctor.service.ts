import { get } from "./core.service";

const ROUTE = "/doctors";

export const get_all_doctors = async () => {
  const uri = ROUTE;

  return await get(uri);
}