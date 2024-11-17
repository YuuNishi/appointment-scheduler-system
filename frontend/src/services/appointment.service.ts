import moment from "moment";
import type {
  CreateAppointment,
  GetByIdResponseType,
  GetByRangeType,
  UpdateAppointment
} from '../types/services/appointment.types';
import { get, post, put, remove } from './core.service';

const ROUTE = "/appointments";

export const get_appointments_by_range = async (data: GetByRangeType) => {
  const uri = ROUTE + "/range";
  
  const params = new URLSearchParams({
    start_date: moment(data.start_date).format('YYYY-MM-DD'),
    end_date: moment(data.end_date).format('YYYY-MM-DD')
  });

  if (data.criteria)
    params.append("criteria", data.criteria as string);

  return await get(uri, params);
}

export const get_appointment_by_id  = async (id: number) => {
  const uri = ROUTE + "/"+ id;

  return await get(uri)
}

export const create_appointment = async (data: CreateAppointment) => {
  const uri = ROUTE + "/";

  return await post(uri, data);
}

export const update_appointment = async (id: number, data: UpdateAppointment) => {
  const uri = ROUTE + "/" + id;

  return await put(uri, data);
}

export const delete_appointment = async (id: number) => {
  const uri = ROUTE + "/" + id;

  return await remove(uri);
}