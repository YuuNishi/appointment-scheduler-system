import UserAvatar from '$lib/assets/placeholder_user.png';
import AssistantAvatar from '$lib/assets/assistant.png';
import FemaleDocAvatar from '$lib/assets/female_doctor.png';
import MaleDocAvatar from '$lib/assets/male_doctor.png';
import { UserAvatarEnum } from '../enums/store.enums';

export function get_avatar_by_enum(avatar: UserAvatarEnum) {
  switch (avatar) {
    case UserAvatarEnum.placeholder:
      return UserAvatar;
    case UserAvatarEnum.assistant:
      return AssistantAvatar;
    case UserAvatarEnum.female_doc:
      return FemaleDocAvatar;
    case UserAvatarEnum.male_doc:
      return MaleDocAvatar;
    default:
      return UserAvatar;
  }
}