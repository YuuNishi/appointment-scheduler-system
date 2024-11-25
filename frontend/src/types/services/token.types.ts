export type CreateTokenType = {
  email: string
  password: string
}

export type KeepAliveTokenType = {
  token: string
}

export type TokenResponse = {
  token: string;
  username: string;
}