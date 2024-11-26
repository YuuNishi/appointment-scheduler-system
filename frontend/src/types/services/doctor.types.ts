export type GetAllDoctorsType = {
  id: number,
  name: string,
  specialty: string
}

export type CreateDoctorType = {
  name: string,
  speciality_id: number
}