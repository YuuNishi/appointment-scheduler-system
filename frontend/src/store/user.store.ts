import { writable } from "svelte/store";
import UserAvatar from '$lib/assets/placeholder_user.png';

export const userInformation = writable({
  username: "usuário",
  avatar: UserAvatar
})