export type CreateTokenType = {
  email: string
  password: string
}

export type TokenResponse = {
  token: string;
  username: string;
}