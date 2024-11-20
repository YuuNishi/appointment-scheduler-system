import type { CreateTokenType, KeepAliveTokenType } from '../types/services/token.types';
import { post, post_literal } from './core.service';

const ROUTE = "/tokens";

export const create_token = async (data: CreateTokenType) => {
  const uri = ROUTE + "/";

  return await post_literal(uri, data);
}

export const keep_alive_token = async (data: KeepAliveTokenType) => {
  const uri = ROUTE + "/keep-alive";

  return await post(uri, data)
}