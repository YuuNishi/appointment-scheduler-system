import { redirect } from '@sveltejs/kit';
import { keep_alive } from './services/core.service';

export const handle = async ({ event, resolve }) => {
  const url = new URL(event.request.url);
  const token = event.cookies.get("token");

    if (!token) {
      if (url.pathname !== "/login") {
        redirect(302, '/login');
      }
    }
    else {
      try {
        const data = await keep_alive(token);

        if (!data.ok) {
          throw new Error();
        }
      } catch {
        if (url.pathname != '/login') {
          redirect(302, '/login');
        }
      }
    }

  return await resolve(event);
};