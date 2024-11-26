import { get, post, remove } from './core.service';
import type { CreateDoctorType } from '../types/services/doctor.types';

const ROUTE = "/doctors";

export const get_all_doctors = async () => {
  const uri = ROUTE;

  return await get(uri);
}

export const create_doctor = async (data: CreateDoctorType) => {
  const uri = ROUTE + "/";

  return await post(uri, data);
}

export const delete_doctor = async (id: string) => {
  const uri = ROUTE + "/" + id;

  return await remove(uri);
}