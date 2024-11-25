export type GetByRangeType = {
  start_date: Date
  end_date: Date
  criteria?: string
}

export type GetByIdResponseType = {
  title: string
  patient_id: number
  doctor_ids: number[]
  type: number
  date: Date
  start_time: string
  duration: number
  paid: number
  status: number
}

export type GetByRangeResponseType = {
  id: number
  date: Date
  start_time: string
  finish_time: string
  title: string
  paid: boolean
}

export type CreateAppointment = {
  patient_id: number
  doctor_ids: number[]
  title: string
  date: string
  start_time: string
  finish_time: string
  type: number
}

export type UpdateAppointment = {
  patient_id: number
  doctor_ids: number[]
  title: string
  date: string
  start_time: string
  finish_time: string
  type: number
  paid: number
}