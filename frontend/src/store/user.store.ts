import { writable } from 'svelte/store';
import { get_avatar_by_enum } from '../utils/avatar.utils';
import { UserAvatarEnum } from '../enums/store.enums';

export const userInformation = writable({
  username: 'user',
  avatar: get_avatar_by_enum(UserAvatarEnum.placeholder)
});