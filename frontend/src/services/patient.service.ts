import { get } from "./core.service";

const ROUTE = "/patients";

export const get_all_patients = async () => {
  const uri = ROUTE;

  return await get(uri);
}