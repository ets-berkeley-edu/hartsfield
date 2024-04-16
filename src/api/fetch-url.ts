import utils from '@/api/api-utils'

export function fetchUrl(gsSourceUrl: string) {
  return utils.post('/api/fetch_url_direct', {gsSourceUrl}, true)
}
