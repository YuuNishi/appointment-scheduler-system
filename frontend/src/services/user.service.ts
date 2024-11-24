import { get, patch, patch_literal } from './core.service';
import type { UpdateAvatarType, UpdatePasswordType, UpdateUsernameType } from '../types/services/user.types';

const ROUTE = "/users";

export const get_user_information = async () => {
  const uri = ROUTE + "/user/info";

  return await get(uri);
}

export const update_password = async (data: UpdatePasswordType) => {
  const uri = ROUTE + "/change/password";

  return await patch_literal(uri, data)
}

export const update_username = async (data: UpdateUsernameType) => {
  const uri = ROUTE + "/change/username";

  return await patch(uri, data)
}

export const update_avatar = async (data: UpdateAvatarType) => {
  const uri = ROUTE + "/change/avatar";

  return await patch(uri, data)
}