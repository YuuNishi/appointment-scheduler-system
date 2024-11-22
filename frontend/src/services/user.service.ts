import { get, patch } from './core.service';
import type { UpdatePasswordType, UpdateUsernameType } from '../types/services/user.types';

const ROUTE = "/users";

export const get_user_information = async () => {
  const uri = ROUTE + "/user/info";

  return await get(uri);
}

export const update_password = async (id: string, data: UpdatePasswordType) => {
  const uri = ROUTE + "/" + id + "/password";

  return await patch(uri, data)
}

export const update_username = async (id: string, data: UpdateUsernameType) => {
  const uri = ROUTE + "/" + id + "/username";

  return await patch(uri, data)
}