import moment from "moment";
import type { CreateAppointment, GetByRangeType } from "../types/services/appointment.types";
import { get, post } from "./core.service";

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

export const create_appointment = async (data: CreateAppointment) => {
  const uri = ROUTE + "/";

  return await post(uri, data);
}