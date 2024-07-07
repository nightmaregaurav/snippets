const url = '';
const numRequests = 10000;

function sendRequest() {
  return fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response;
    })
    .then(response => console.log(`Status: ${response.status}`))
    .catch(error => console.error(`Error: ${error.message}`));
}

async function main() {
  const requests = Array.from({ length: numRequests }, () => sendRequest());
  await Promise.all(requests);
  console.log(`${numRequests} requests completed.`);
}

main();
