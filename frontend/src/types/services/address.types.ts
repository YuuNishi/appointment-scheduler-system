export type CreateAddressType = {
    cep: string,
    street: string,
    neighborhood: string,
    city: string,
    federal_unit: string,
    number: number
}

export type AddressResponseType = {
    id: number
}