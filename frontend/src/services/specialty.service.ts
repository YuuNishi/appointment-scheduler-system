import { get, post } from './core.service';
import type { CreateSpecialtyType } from '../types/services/specialty.types';

const ROUTE = "/specialties";

export const get_all_specialties = async () => {
  const uri = ROUTE;

  return await get(uri);
}

export const create_specialty = async (data: CreateSpecialtyType) => {
  const uri = ROUTE + "/";

  return await post(uri, data);
}