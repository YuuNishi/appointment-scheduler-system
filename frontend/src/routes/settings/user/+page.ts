import type { PageLoad } from './$types';
import { get_user_information } from '../../../services/user.service';

export const load: PageLoad = async () => {
  const data = await get_user_information();

  return {
    userInfo: await data.json()
  };
}