// TODO: Add link to openapi/swagger
const BASE_URL = 'http://localhost:8000'

const headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

async function postLightFill(body) {
  fetch(`${BASE_URL}/lights/fill`, {
    method: 'POST',
    headers,
    body: JSON.stringify(body)
  })
    .then(response => response.json())
    .then(response => console.log(JSON.stringify(response)))
}

async function postLightFillByIndex(body) {
  fetch(`${BASE_URL}/lights/fill_by_index`, {
    method: 'POST',
    headers,
    body: JSON.stringify(body)
  })
    .then(response => response.json())
    .then(response => console.log(JSON.stringify(response)))
}

async function postLightScrollingText(body) {
  fetch(`${BASE_URL}/lights/scrolling_text`, {
    method: 'POST',
    headers,
    body: JSON.stringify(body)
  })
    .then(response => response.json())
    .then(response => console.log(JSON.stringify(response)))
}

async function postLightRainbow(body) {
  fetch(`${BASE_URL}/lights/rainbow`, {
    method: 'POST',
    headers,
    body: JSON.stringify(body)
  })
    .then(response => response.json())
    .then(response => console.log(JSON.stringify(response)))
}

async function postLightColorCycle(body) {
  fetch(`${BASE_URL}/lights/color_cycle`, {
    method: 'POST',
    headers,
    body: JSON.stringify(body)
  })
    .then(response => response.json())
    .then(response => console.log(JSON.stringify(response)))
}
