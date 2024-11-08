export type GetByRangeType = {
  start_date: Date,
  end_date: Date,
  criteria?: string
}

export type GetByRangeResponseType = {
  id: number,
  date: Date,
  start_time: string,
  finish_time: string,
  title: string,
  paid: boolean
}

export type CreateAppointment = {
  patient_id: number
  doctor_ids: number[]
  created_by: string
  title: string
  date: string
  start_time: string
  finish_time: string
  type: number
}