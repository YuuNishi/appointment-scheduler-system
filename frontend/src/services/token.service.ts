import type { CreateTokenType } from '../types/services/token.types';
import { post } from './core.service';

const ROUTE = "/tokens";

export const create_token = async (data: CreateTokenType) => {
  const uri = ROUTE + "/";

  return await post(uri, data);
}