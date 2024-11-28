export type GetAllPatientType = {
  id: number,
  name: string,
  status: number,
  sex: number,
  birth_date: Date,
  CPF: string
}
export type CreatePatientType = {
  name: string,
  status: number,
  sex: number,
  birth_date: Date,
  cpf: string,
  address_id: number
}
export type UpdatePatientType = {
  name: string,
  status: number,
  sex: number,
  birth_date: string,
  cpf: string,
  address_id: number
}

