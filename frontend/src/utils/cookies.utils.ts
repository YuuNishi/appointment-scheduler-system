import moment from 'moment/moment';

export const setCookie = (name: string, value: string, days: number) => {
  const date = moment.utc().add(1, 'hour');
  const expires = `expires=${date.toISOString()}`;
  if (typeof window !== 'undefined') {
    document.cookie = `${name}=${value};${expires};path=/`;
  }
};

export const getCookie = (name: string) => {
  if (typeof window !== 'undefined') {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
      return parts.pop()?.split(';').shift() || null;
    }
  }
  return null;
}

export const deleteCookie = (name: string) => {
  if (typeof window !== 'undefined') {
    document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
  }
};