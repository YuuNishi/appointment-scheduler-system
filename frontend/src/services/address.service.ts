import { post} from "./core.service";
import type { CreateAddressType } from "../types/services/address.types";
const ROUTE = "/address";

export const create_address = async (address: CreateAddressType) => {
  const uri = ROUTE + '/';

  return await post(uri, address);
}