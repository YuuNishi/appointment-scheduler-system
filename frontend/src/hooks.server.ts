import { redirect } from '@sveltejs/kit';
import { keep_alive_token } from './services/token.service';
import type { TokenResponse } from './types/services/token.types';
import moment from 'moment';

const public_paths = ['/login'];

function isPathAllowed(path: string) {
  return public_paths.some(
    (allowedPath) => path === allowedPath || path.startsWith(allowedPath + '/')
  );
}

export const handle = async ({ event, resolve }) => {
  const token = event.cookies.get('token');
  const token_creation = event.cookies.get('token_create');

  const url = new URL(event.request.url);

  if (!token && !isPathAllowed(url.pathname)) {
    throw redirect(302, '/login');
  }

  if (token) {
    let isValidTime = false;

    if (token_creation) {
      try {
        const decoded_token = decodeURIComponent(token_creation);

        const diff = moment.utc().diff(moment(decoded_token), 'minutes');
        isValidTime = diff <= 50;
      } catch {
        if (url.pathname != '/login') {
          throw redirect(302, '/login');
        }
      }
    }

    if (!isValidTime) {
      const keepAliveResponse = await keep_alive_token({ token });

      if (keepAliveResponse.ok) {
        const data: TokenResponse = await keepAliveResponse.json();

        const expDate = moment.utc().add(1, 'hour');

        event.cookies.set('token', data.token, {
          path: '/',
          expires: expDate.toDate(),
          httpOnly: false
        });

        event.cookies.set('token_create', moment.utc().toISOString(), {
          path: '/',
          expires: expDate.toDate(),
          httpOnly: false
        });
      } else {
        if (url.pathname != '/login') {
          throw redirect(302, '/login');
        }
      }
    }

    if (url.pathname == '/login') {
      throw redirect(302, '/appointments');
    }
  }

  return await resolve(event);
};