import type { CreatePatientType, UpdatePatientType } from "../types/services/patient.types";
import { get,post, put, remove } from "./core.service";

const ROUTE = "/patients";

export const get_all_patients = async () => {
  const uri = ROUTE;

  return await get(uri);
}

export const remove_patient = async (id:number) => {
  const uri = ROUTE + `/${id}`;

  return await remove(uri);
}

export const create_patient = async (patient: CreatePatientType) => {
  const uri = ROUTE + '/';

  return await post(uri,patient);
}
export const update_patient = async (patient: UpdatePatientType, id: number) => {
  const uri = ROUTE + `/${id}`;

  return await put(uri,patient);
}
