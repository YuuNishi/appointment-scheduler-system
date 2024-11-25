import type { UserAvatarEnum } from '../../enums/store.enums';

export type UpdatePasswordType = {
  oldPassword: string
  newPassword: string
}

export type UpdateUsernameType = {
  username: string
}

export type UpdateAvatarType = {
  avatar: UserAvatarEnum
}

export type UserResponseType = {
  username: string
}