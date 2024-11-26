import type { PageLoad } from './$types';
import { get_all_doctors } from '../../../services/doctor.service';

export const load: PageLoad = async () => {
  const doctors = await get_all_doctors();

  return {
    doctors: await doctors.json()
  };
}