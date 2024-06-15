const client = require('@sendgrid/client');
// const ApiKey = "";
client.setApiKey(ApiKey)

const request = {
  url: `/v3/scopes`,
  method: 'GET',
}

client.request(request)
  .then(([response, _]) => {
    console.log(response);
  })
  .catch(error => {
    console.error(error);
  });